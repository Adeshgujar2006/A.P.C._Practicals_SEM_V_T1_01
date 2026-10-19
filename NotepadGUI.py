import datetime
import os
import textwrap
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font as tkfont

BASE_SIZE = 12                 
MIN_SIZE, MAX_SIZE = 6, 80
FILETYPES = [("Text Documents", "*.txt"), ("All Files", "*.*")]

def text_to_pdf(text, path, font_size=11):

    page_w, page_h, margin = 595, 842, 50
    leading = font_size * 1.4
    chars_per_line = int((page_w - 2 * margin) / (0.6 * font_size))   # Courier = 0.6 em
    lines_per_page = int((page_h - 2 * margin) / leading)

    lines = []
    for raw in text.expandtabs(4).splitlines() or [""]:
        lines.extend(textwrap.wrap(raw, chars_per_line, replace_whitespace=False,
                                   drop_whitespace=False) or [""])
    pages = [lines[i:i + lines_per_page] for i in range(0, len(lines), lines_per_page)] or [[""]]

    kids = " ".join(f"{4 + 2 * i} 0 R" for i in range(len(pages)))
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>".encode(),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>",
    ]
    for i, page_lines in enumerate(pages):
        objs.append((f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {page_w} {page_h}] "
                     f"/Resources << /Font << /F1 3 0 R >> >> /Contents {5 + 2 * i} 0 R >>").encode())
        stream = bytearray(
            f"BT /F1 {font_size} Tf {leading:.1f} TL {margin} {page_h - margin - font_size} Td\n".encode())
        for line in page_lines:
            safe = (line.encode("cp1252", "replace")
                    .replace(b"\\", b"\\\\").replace(b"(", b"\\(").replace(b")", b"\\)"))
            stream += b"(" + safe + b") Tj T*\n"
        stream += b"ET"
        objs.append(f"<< /Length {len(stream)} >>\nstream\n".encode() + bytes(stream) + b"\nendstream")

    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for num, body in enumerate(objs, start=1):
        offsets.append(len(out))
        out += f"{num} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
    for off in offsets:
        out += f"{off:010d} 00000 n \n".encode()
    out += (f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref}\n%%EOF\n").encode()
    with open(path, "wb") as f:
        f.write(out)



class Notepad:
    def __init__(self, root):
        self.root = root
        self.filepath = None
        self.font_size = BASE_SIZE
        self.find_win = None

        families = set(tkfont.families(root))
        self.fonts = [f for f in ("Consolas", "Courier New", "Arial", "Calibri",
                                  "Times New Roman", "DejaVu Sans Mono") if f in families]
        default = self.fonts[0] if self.fonts else tkfont.nametofont("TkFixedFont").actual("family")
        self.font_var = tk.StringVar(value=default)
        self.font = tkfont.Font(family=default, size=self.font_size)

        root.geometry("800x550")

        
        self.status = tk.Label(root, anchor="e", relief="sunken", padx=8)
        self.status.pack(side="bottom", fill="x")

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.text = tk.Text(self.frame, wrap="word", undo=True, font=self.font,
                            padx=6, pady=4, maxundo=-1)
        self.vscroll = tk.Scrollbar(self.frame, command=self.text.yview)
        self.hscroll = tk.Scrollbar(self.frame, orient="horizontal", command=self.text.xview)
        self.text.config(yscrollcommand=self.vscroll.set, xscrollcommand=self.hscroll.set)
        self.text.grid(row=0, column=0, sticky="nsew")
        self.vscroll.grid(row=0, column=1, sticky="ns")
        self.hscroll.grid(row=1, column=0, sticky="ew")
        self.hscroll.grid_remove()                       # only needed when word wrap is off
        self.text.tag_config("found", background="yellow", foreground="black")

        self.wrap_var = tk.BooleanVar(value=True)
        self.status_var = tk.BooleanVar(value=True)

        self.build_menu()
        self.bind_keys()
        self.text.focus_set()
        self.update_title()
        self.update_status()
        root.protocol("WM_DELETE_WINDOW", self.exit_app)

    
    def build_menu(self):
        bar = tk.Menu(self.root)
        self.root.config(menu=bar)

        m = tk.Menu(bar, tearoff=0)
        bar.add_cascade(label="File", menu=m)
        m.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        m.add_command(label="Open...", accelerator="Ctrl+O", command=self.open_file)
        m.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        m.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=self.save_as)
        m.add_separator()
        m.add_command(label="Export as PDF...", accelerator="Ctrl+P", command=self.export_pdf)
        m.add_separator()
        m.add_command(label="Exit", command=self.exit_app)

        m = tk.Menu(bar, tearoff=0)
        bar.add_cascade(label="Edit", menu=m)
        m.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undo)
        m.add_command(label="Redo", accelerator="Ctrl+Y", command=self.redo)
        m.add_separator()
        m.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.text.event_generate("<<Cut>>"))
        m.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.text.event_generate("<<Copy>>"))
        m.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.text.event_generate("<<Paste>>"))
        m.add_command(label="Delete", accelerator="Del", command=self.delete_selection)
        m.add_separator()
        m.add_command(label="Find / Replace...", accelerator="Ctrl+F", command=self.find_dialog)
        m.add_command(label="Select All", accelerator="Ctrl+A", command=self.select_all)
        m.add_command(label="Time/Date", accelerator="F5", command=self.insert_datetime)

        m = tk.Menu(bar, tearoff=0)
        bar.add_cascade(label="Format", menu=m)
        m.add_checkbutton(label="Word Wrap", variable=self.wrap_var, command=self.toggle_wrap)
        font_menu = tk.Menu(m, tearoff=0)
        m.add_cascade(label="Font", menu=font_menu)
        for name in self.fonts:
            font_menu.add_radiobutton(label=name, value=name, variable=self.font_var,
                                      command=lambda: self.font.configure(family=self.font_var.get()))

        m = tk.Menu(bar, tearoff=0)
        bar.add_cascade(label="View", menu=m)
        zoom = tk.Menu(m, tearoff=0)
        m.add_cascade(label="Zoom", menu=zoom)
        zoom.add_command(label="Zoom In", accelerator="Ctrl++", command=lambda: self.zoom(2))
        zoom.add_command(label="Zoom Out", accelerator="Ctrl+-", command=lambda: self.zoom(-2))
        zoom.add_command(label="Restore Default Zoom", accelerator="Ctrl+0", command=self.zoom_reset)
        m.add_checkbutton(label="Status Bar", variable=self.status_var, command=self.toggle_status)

        m = tk.Menu(bar, tearoff=0)
        bar.add_cascade(label="Help", menu=m)
        m.add_command(label="About Notepad", command=lambda: messagebox.showinfo(
            "About Notepad", "Created by a student using tkinter"))

        
        self.popup = tk.Menu(self.root, tearoff=0)
        self.popup.add_command(label="Cut", command=lambda: self.text.event_generate("<<Cut>>"))
        self.popup.add_command(label="Copy", command=lambda: self.text.event_generate("<<Copy>>"))
        self.popup.add_command(label="Paste", command=lambda: self.text.event_generate("<<Paste>>"))
        self.popup.add_separator()
        self.popup.add_command(label="Select All", command=self.select_all)
        for button in ("<Button-3>", "<Button-2>"):
            self.text.bind(button, lambda e: self.popup.tk_popup(e.x_root, e.y_root))

    def bind_keys(self):
        r = self.root
        r.bind("<Control-n>", lambda e: self.new_file())
        r.bind("<Control-o>", lambda e: self.open_file())
        r.bind("<Control-s>", lambda e: self.save_file())
        r.bind("<Control-S>", lambda e: self.save_as())
        r.bind("<Control-p>", lambda e: self.export_pdf())
        r.bind("<Control-f>", lambda e: self.find_dialog())
        r.bind("<Control-y>", lambda e: self.redo())
        r.bind("<F5>", lambda e: self.insert_datetime())
        self.text.bind("<Control-a>", lambda e: self.select_all())

        for seq in ("<Control-plus>", "<Control-equal>", "<Control-KP_Add>"):
            r.bind(seq, lambda e: self.zoom(2))
        for seq in ("<Control-minus>", "<Control-KP_Subtract>"):
            r.bind(seq, lambda e: self.zoom(-2))
        r.bind("<Control-Key-0>", lambda e: self.zoom_reset())
        self.text.bind("<Control-MouseWheel>", self.wheel_zoom)                 # Windows / macOS
        self.text.bind("<Control-Button-4>", lambda e: self.zoom(2) or "break")  # Linux
        self.text.bind("<Control-Button-5>", lambda e: self.zoom(-2) or "break")

        self.text.bind("<<Modified>>", self.on_modified)
        for seq in ("<KeyRelease>", "<ButtonRelease-1>"):
            self.text.bind(seq, self.update_status)

    
    def update_title(self):
        name = os.path.basename(self.filepath) if self.filepath else "Untitled"
        star = "*" if self.text.edit_modified() else ""
        self.root.title(f"{star}{name} - Notepad")

    def on_modified(self, event=None):
        self.update_title()
        self.update_status()

    def update_status(self, event=None):
        line, col = self.text.index("insert").split(".")
        words = len(self.text.get("1.0", "end-1c").split())
        pct = round(self.font_size / BASE_SIZE * 100)
        self.status.config(text=f"Ln {line}, Col {int(col) + 1}     Words: {words}     "
                                f"Zoom: {pct}%     UTF-8")

    def toggle_status(self):
        if self.status_var.get():
            self.status.pack(side="bottom", fill="x", before=self.frame)
        else:
            self.status.pack_forget()


    def confirm_discard(self):
        
        if not self.text.edit_modified():
            return True
        name = os.path.basename(self.filepath) if self.filepath else "Untitled"
        answer = messagebox.askyesnocancel("Notepad", f"Do you want to save changes to {name}?")
        if answer is None:
            return False
        return self.save_file() if answer else True

    def new_file(self):
        if not self.confirm_discard():
            return
        self.text.delete("1.0", "end")
        self.filepath = None
        self.text.edit_reset()
        self.text.edit_modified(False)
        self.update_title()

    def open_file(self):
        if not self.confirm_discard():
            return
        path = filedialog.askopenfilename(filetypes=FILETYPES)
        if not path:
            return
        try:
            try:
                with open(path, encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(path, encoding="latin-1") as f:
                    content = f.read()
        except OSError as e:
            messagebox.showerror("Open", f"Could not open the file:\n{e}")
            return
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)
        self.text.edit_reset()
        self.text.edit_modified(False)
        self.filepath = path
        self.update_title()
        self.update_status()

    def save_file(self):
        if not self.filepath:
            return self.save_as()
        return self.write_file(self.filepath)

    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=FILETYPES)
        if not path:
            return False
        return self.write_file(path)

    def write_file(self, path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", "end-1c"))
        except OSError as e:
            messagebox.showerror("Save", f"Could not save the file:\n{e}")
            return False
        self.filepath = path
        self.text.edit_modified(False)
        self.update_title()
        return True

    def export_pdf(self):
        content = self.text.get("1.0", "end-1c")
        base = os.path.splitext(os.path.basename(self.filepath))[0] if self.filepath else "Untitled"
        path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=base + ".pdf",
                                            filetypes=[("PDF Document", "*.pdf")])
        if not path:
            return
        try:
            content.encode("cp1252")
        except UnicodeEncodeError:
            messagebox.showwarning("Export as PDF", "Some characters (for example Marathi/Hindi text) "
                                   "are not supported in the PDF and will appear as '?'.")
        try:
            text_to_pdf(content, path)
        except OSError as e:
            messagebox.showerror("Export as PDF", f"Could not create the PDF:\n{e}")
            return
        messagebox.showinfo("Export as PDF", f"PDF saved:\n{path}")

    def exit_app(self):
        if self.confirm_discard():
            self.root.destroy()

    
    def undo(self):
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def delete_selection(self):
        if self.text.tag_ranges("sel"):
            self.text.delete("sel.first", "sel.last")

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end-1c")
        return "break"

    def insert_datetime(self):
        self.text.insert("insert", datetime.datetime.now().strftime("%I:%M %p %d-%m-%Y"))

    
    def find_dialog(self):
        if self.find_win and self.find_win.winfo_exists():
            self.find_win.lift()
            return
        win = self.find_win = tk.Toplevel(self.root)
        win.title("Find and Replace")
        win.transient(self.root)
        win.resizable(False, False)

        self.find_var, self.repl_var, self.case_var = tk.StringVar(), tk.StringVar(), tk.BooleanVar()
        if self.text.tag_ranges("sel"):
            self.find_var.set(self.text.get("sel.first", "sel.last"))

        tk.Label(win, text="Find what:").grid(row=0, column=0, padx=8, pady=6, sticky="w")
        entry = tk.Entry(win, textvariable=self.find_var, width=28)
        entry.grid(row=0, column=1, padx=8, pady=6)
        tk.Label(win, text="Replace with:").grid(row=1, column=0, padx=8, pady=6, sticky="w")
        tk.Entry(win, textvariable=self.repl_var, width=28).grid(row=1, column=1, padx=8, pady=6)
        tk.Checkbutton(win, text="Match case", variable=self.case_var).grid(
            row=2, column=0, columnspan=2, padx=8, sticky="w")

        buttons = tk.Frame(win)
        buttons.grid(row=3, column=0, columnspan=2, pady=8)
        tk.Button(buttons, text="Find Next", width=10, command=self.find_next).pack(side="left", padx=4)
        tk.Button(buttons, text="Replace", width=10, command=self.replace_one).pack(side="left", padx=4)
        tk.Button(buttons, text="Replace All", width=10, command=self.replace_all).pack(side="left", padx=4)

        win.bind("<Return>", lambda e: self.find_next())
        win.bind("<Escape>", lambda e: win.destroy())
        win.protocol("WM_DELETE_WINDOW", lambda: (self.text.tag_remove("found", "1.0", "end"), win.destroy()))
        entry.focus_set()

    def find_next(self):
        needle = self.find_var.get()
        self.text.tag_remove("found", "1.0", "end")
        if not needle:
            return False
        nocase = not self.case_var.get()
        pos = self.text.search(needle, "insert", stopindex="end", nocase=nocase)
        if not pos:                                   # wrap around to the top
            pos = self.text.search(needle, "1.0", stopindex="end", nocase=nocase)
        if not pos:
            messagebox.showinfo("Find", f'Cannot find "{needle}"', parent=self.find_win)
            return False
        end = f"{pos}+{len(needle)}c"
        self.text.tag_remove("sel", "1.0", "end")
        self.text.tag_add("sel", pos, end)
        self.text.tag_add("found", pos, end)
        self.text.mark_set("insert", end)
        self.text.see(pos)
        return True

    def replace_one(self):
        needle = self.find_var.get()
        if self.text.tag_ranges("sel"):
            chosen = self.text.get("sel.first", "sel.last")
            same = chosen == needle if self.case_var.get() else chosen.lower() == needle.lower()
            if needle and same:
                start = self.text.index("sel.first")
                self.text.delete("sel.first", "sel.last")
                self.text.insert(start, self.repl_var.get())
                self.text.mark_set("insert", f"{start}+{len(self.repl_var.get())}c")
        self.find_next()

    def replace_all(self):
        needle, repl = self.find_var.get(), self.repl_var.get()
        if not needle:
            return
        nocase = not self.case_var.get()
        pos, count = "1.0", 0
        while True:
            pos = self.text.search(needle, pos, stopindex="end", nocase=nocase)
            if not pos:
                break
            self.text.delete(pos, f"{pos}+{len(needle)}c")
            self.text.insert(pos, repl)
            pos = f"{pos}+{len(repl)}c"
            count += 1
        messagebox.showinfo("Replace All", f"Replaced {count} occurrence(s).", parent=self.find_win)

    
    def toggle_wrap(self):
        if self.wrap_var.get():
            self.text.config(wrap="word")
            self.hscroll.grid_remove()
        else:
            self.text.config(wrap="none")
            self.hscroll.grid()

    def zoom(self, delta):
        self.font_size = max(MIN_SIZE, min(MAX_SIZE, self.font_size + delta))
        self.font.configure(size=self.font_size)
        self.update_status()
        return "break"

    def zoom_reset(self):
        self.font_size = BASE_SIZE
        self.font.configure(size=BASE_SIZE)
        self.update_status()
        return "break"

    def wheel_zoom(self, event):
        return self.zoom(2 if event.delta > 0 else -2)


if __name__ == "__main__":
    root = tk.Tk()
    Notepad(root)
    root.mainloop()
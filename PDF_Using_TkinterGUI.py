
import bisect
import os
import sys
from collections import OrderedDict
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

try:
    import pymupdf as fitz
except ImportError:
    try:
        import fitz
    except ImportError:
        fitz = None
try:
    from PIL import Image, ImageTk
except ImportError:
    Image = ImageTk = None

MIN_ZOOM, MAX_ZOOM, ZOOM_STEP = 0.25, 5.0, 1.25   
PAD = 20                                            
THUMB_W, THUMB_PAD, THUMB_LABEL, SIDEBAR_W = 110, 14, 20, 150
CACHE_PAGES = 8


class PDFViewer:
    def __init__(self, root):
        self.root = root
        self.doc = None
        self.path = None
        self.page_no = 0
        self.zoom = 1.0
        self.fit_mode = "width"            # "width", "page" or None (manual zoom)
        self.rotation = 0                  # extra rotation chosen by the user
        self.base_rot = []
        self.sizes = []                    # page sizes in points (width, height)
        self.max_w = 1
        # main view layout
        self.offsets, self.widths, self.heights = [], [], []
        self.total_h, self.content_w = 0, 0
        self.drawn, self.cache = set(), OrderedDict()
        self.pending = None                # page requested by go_to() until the user scrolls
        self.view_job = self.thumb_job = self.resize_job = None
        # thumbnails
        self.thumb_offsets, self.thumb_heights, self.thumb_total = [], [], 0
        self.thumb_drawn = {}
        # search
        self.hits, self.hits_by_page, self.hit_idx, self.query, self.match_text = [], {}, -1, "", ""
        self.sidebar_on = tk.BooleanVar(value=True)

        root.geometry("1150x720")
        self.build_menu()
        self.build_toolbar()
        self.build_body()
        self.bind_keys()
        self.update_status()

    # ------------------------------------------------------------------ UI
    def build_menu(self):
        bar = tk.Menu(self.root)
        self.root.config(menu=bar)
        m = tk.Menu(bar, tearoff=0)
        bar.add_cascade(label="File", menu=m)
        m.add_command(label="Open...", accelerator="Ctrl+O", command=self.open_pdf)
        m.add_command(label="Save Page as Image...", accelerator="Ctrl+S", command=self.save_image)
        m.add_separator()
        m.add_command(label="Exit", command=self.exit_app)

        m = tk.Menu(bar, tearoff=0)
        bar.add_cascade(label="View", menu=m)
        m.add_command(label="Zoom In", accelerator="Ctrl++", command=lambda: self.zoom_by(ZOOM_STEP))
        m.add_command(label="Zoom Out", accelerator="Ctrl+-", command=lambda: self.zoom_by(1 / ZOOM_STEP))
        m.add_command(label="Actual Size (100%)", accelerator="Ctrl+0", command=self.zoom_reset)
        m.add_command(label="Fit Width", accelerator="Ctrl+1", command=lambda: self.set_fit("width"))
        m.add_command(label="Fit Page", accelerator="Ctrl+2", command=lambda: self.set_fit("page"))
        m.add_separator()
        m.add_command(label="Rotate", accelerator="Ctrl+R", command=self.rotate)
        m.add_checkbutton(label="Page Thumbnails", accelerator="F4", variable=self.sidebar_on,
                          command=self.toggle_sidebar)

    def build_toolbar(self):
        bar = tk.Frame(self.root, padx=4, pady=4)
        bar.pack(side="top", fill="x")

        def button(text, cmd, width=None):
            b = tk.Button(bar, text=text, command=cmd, width=width)
            b.pack(side="left", padx=2)
            return b

        def sep():
            tk.Frame(bar, width=2, bd=1, relief="sunken").pack(side="left", fill="y", padx=6)

        button("Open", self.open_pdf)
        button("☰ Pages", self.toggle_sidebar_button)
        sep()
        button("◀", lambda: self.go_to(self.page_no - 1), 3)
        self.page_var = tk.StringVar()
        self.page_entry = tk.Entry(bar, textvariable=self.page_var, width=5, justify="center")
        self.page_entry.pack(side="left")
        self.page_entry.bind("<Return>", self.goto_entry)
        self.total_label = tk.Label(bar, text="/ 0")
        self.total_label.pack(side="left", padx=2)
        button("▶", lambda: self.go_to(self.page_no + 1), 3)
        sep()
        button("−", lambda: self.zoom_by(1 / ZOOM_STEP), 3)
        self.zoom_label = tk.Label(bar, text="100%", width=6)
        self.zoom_label.pack(side="left")
        button("+", lambda: self.zoom_by(ZOOM_STEP), 3)
        button("Fit Width", lambda: self.set_fit("width"))
        button("Fit Page", lambda: self.set_fit("page"))
        button("Rotate", self.rotate)
        sep()
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(bar, textvariable=self.search_var, width=14)
        self.search_entry.pack(side="left")
        self.search_entry.bind("<Return>", lambda e: self.find(1))
        self.search_entry.bind("<Shift-Return>", lambda e: self.find(-1))
        button("Find", lambda: self.find(1))
        button("▲", lambda: self.find(-1), 2)

    def build_body(self):
        self.status = tk.Label(self.root, anchor="w", relief="sunken", padx=8)
        self.status.pack(side="bottom", fill="x")

        body = tk.Frame(self.root)
        body.pack(fill="both", expand=True)
        body.rowconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)

        # thumbnail sidebar (left)
        self.sidebar = tk.Frame(body)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.tcanvas = tk.Canvas(self.sidebar, width=SIDEBAR_W, bg="#3c3c3c", highlightthickness=0,
                                 yscrollincrement=30)
        self.ts = tk.Scrollbar(self.sidebar, command=self.tcanvas.yview)
        self.tcanvas.config(yscrollcommand=self.on_tscroll)
        self.tcanvas.pack(side="left", fill="y")
        self.ts.pack(side="left", fill="y")
        self.tcanvas.bind("<Button-1>", self.on_thumb_click)
        self.tcanvas.bind("<Configure>", lambda e: self.update_thumbs())

        # main page view (right)
        main = tk.Frame(body)
        main.grid(row=0, column=1, sticky="nsew")
        main.rowconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(main, bg="#6b6b6b", highlightthickness=0, cursor="fleur", yscrollincrement=30)
        self.vs = tk.Scrollbar(main, command=self.canvas.yview)
        self.hs = tk.Scrollbar(main, orient="horizontal", command=self.canvas.xview)
        self.canvas.config(yscrollcommand=self.on_yscroll, xscrollcommand=self.hs.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.vs.grid(row=0, column=1, sticky="ns")
        self.hs.grid(row=1, column=0, sticky="ew")
        self.vs.bind("<ButtonPress-1>", lambda e: setattr(self, "pending", None), add="+")
        self.canvas.bind("<Configure>", self.on_resize)
        self.canvas.bind("<ButtonPress-1>", lambda e: (self.canvas.focus_set(), self.canvas.scan_mark(e.x, e.y)))
        self.canvas.bind("<B1-Motion>", self.on_drag)

    def bind_keys(self):
        r = self.root
        r.bind("<Control-o>", lambda e: self.open_pdf())
        r.bind("<Control-s>", lambda e: self.save_image())
        r.bind("<Control-f>", lambda e: (self.search_entry.focus_set(), self.search_entry.select_range(0, "end")))
        r.bind("<F3>", lambda e: self.find(1))
        r.bind("<Shift-F3>", lambda e: self.find(-1))
        r.bind("<F4>", lambda e: (self.sidebar_on.set(not self.sidebar_on.get()), self.toggle_sidebar()))
        r.bind("<Control-r>", lambda e: self.rotate())
        r.bind("<Control-Key-1>", lambda e: self.set_fit("width"))
        r.bind("<Control-Key-2>", lambda e: self.set_fit("page"))
        r.bind("<Control-Key-0>", lambda e: self.zoom_reset())
        for seq in ("<Control-plus>", "<Control-equal>", "<Control-KP_Add>"):
            r.bind(seq, lambda e: self.zoom_by(ZOOM_STEP))
        for seq in ("<Control-minus>", "<Control-KP_Subtract>"):
            r.bind(seq, lambda e: self.zoom_by(1 / ZOOM_STEP))

        def nav(fn):                               # ignore keys while typing in a text box
            return lambda e: None if isinstance(r.focus_get(), tk.Entry) else fn()

        r.bind("<Left>", nav(lambda: self.go_to(self.page_no - 1)))
        r.bind("<Right>", nav(lambda: self.go_to(self.page_no + 1)))
        r.bind("<Home>", nav(lambda: self.go_to(0)))
        r.bind("<End>", nav(lambda: self.go_to(self.page_count() - 1)))
        r.bind("<Up>", nav(lambda: self.scroll_main(-3, "units")))
        r.bind("<Down>", nav(lambda: self.scroll_main(3, "units")))
        r.bind("<Prior>", nav(lambda: self.scroll_main(-1, "pages")))
        r.bind("<Next>", nav(lambda: self.scroll_main(1, "pages")))

        r.bind_all("<MouseWheel>", self.on_wheel)                 # Windows / macOS
        r.bind_all("<Button-4>", lambda e: self.on_wheel(e, -1))  # Linux
        r.bind_all("<Button-5>", lambda e: self.on_wheel(e, 1))
        r.protocol("WM_DELETE_WINDOW", self.exit_app)

    # -------------------------------------------------------------- helpers
    def page_count(self):
        return self.doc.page_count if self.doc else 0

    def eff_size(self, i):
        w, h = self.sizes[i]
        return (h, w) if self.rotation % 180 else (w, h)

    def canvas_size(self):
        return max(self.canvas.winfo_width(), 200), max(self.canvas.winfo_height(), 200)

    def prepare(self, i):
        """Return page i with the right rotation applied."""
        page = self.doc[i]
        page.set_rotation((self.base_rot[i] + self.rotation) % 360)
        return page

    def update_status(self):
        pct = round(self.zoom * 100)
        self.zoom_label.config(text=f"{pct}%")
        self.total_label.config(text=f"/ {self.page_count()}")
        if self.doc:
            if self.root.focus_get() is not self.page_entry:
                self.page_var.set(str(self.page_no + 1))
            name = os.path.basename(self.path)
            text = (f"{name}   |   Page {self.page_no + 1} of {self.page_count()}"
                    f"   |   Zoom {pct}%   |   Rotation {self.rotation}°")
            self.status.config(text=text + (f"   |   {self.match_text}" if self.match_text else ""))
            self.root.title(f"{name} - PDF Viewer")
        else:
            self.status.config(text="No PDF open. Use File > Open (Ctrl+O).")
            self.root.title("PDF Viewer")

    # ----------------------------------------------------------- open / save
    def open_pdf(self, path=None):
        path = path or filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        if not path:
            return
        try:
            doc = fitz.open(path)
            while doc.needs_pass:
                pw = simpledialog.askstring("Password", "This PDF is password protected.\nEnter password:",
                                            show="*", parent=self.root)
                if pw is None:
                    doc.close()
                    return
                if not doc.authenticate(pw):
                    messagebox.showerror("Password", "Wrong password, try again.")
            if doc.page_count == 0:
                raise ValueError("The PDF has no pages.")
        except Exception as e:
            messagebox.showerror("Open PDF", f"Could not open the file:\n{e}")
            return

        if self.doc:
            self.doc.close()
        self.doc, self.path = doc, path
        self.base_rot = [doc[i].rotation for i in range(doc.page_count)]
        self.sizes = [(doc[i].rect.width, doc[i].rect.height) for i in range(doc.page_count)]
        self.page_no, self.rotation, self.fit_mode, self.pending = 0, 0, "width", None
        self.hits, self.hits_by_page, self.hit_idx, self.query, self.match_text = [], {}, -1, "", ""
        self.offsets = []
        self.root.update_idletasks()
        self.relayout(keep_position=False, thumbs=True)
        self.canvas.yview_moveto(0)
        self.tcanvas.yview_moveto(0)

    def save_image(self):
        if not self.doc:
            return
        base = os.path.splitext(os.path.basename(self.path))[0]
        out = filedialog.asksaveasfilename(defaultextension=".png", initialfile=f"{base}_page{self.page_no + 1}.png",
                                           filetypes=[("PNG image", "*.png")])
        if not out:
            return
        self.prepare(self.page_no).get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(out)
        messagebox.showinfo("Save Page as Image", f"Saved:\n{out}")

    def exit_app(self):
        if self.doc:
            self.doc.close()
        self.root.destroy()

    # ---------------------------------------------------- layout & rendering
    def apply_fit(self):
        cw, ch = self.canvas_size()
        if self.fit_mode == "width":
            self.zoom = (cw - 2 * PAD) / self.max_w
        elif self.fit_mode == "page":
            w, h = self.eff_size(self.page_no)
            self.zoom = min((cw - 2 * PAD) / w, (ch - 2 * PAD) / h)
        self.zoom = max(MIN_ZOOM, min(MAX_ZOOM, self.zoom))

    def relayout(self, keep_position=True, thumbs=False):
        """Recalculate where every page sits for the current zoom/rotation and redraw."""
        if not self.doc:
            return
        anchor = None
        if keep_position and self.offsets:                         # remember what the reader is looking at
            top = self.canvas.canvasy(0)
            p = max(0, bisect.bisect_right(self.offsets, top) - 1)
            anchor = (p, (top - self.offsets[p]) / self.heights[p], self.canvas.xview()[0])

        n = self.page_count()
        self.max_w = max(self.eff_size(i)[0] for i in range(n))
        self.apply_fit()
        cw, _ = self.canvas_size()
        self.widths = [self.eff_size(i)[0] * self.zoom for i in range(n)]
        self.heights = [self.eff_size(i)[1] * self.zoom for i in range(n)]
        self.offsets, y = [], PAD
        for h in self.heights:
            self.offsets.append(y)
            y += h + PAD
        self.total_h = y
        self.content_w = max(cw, max(self.widths) + 2 * PAD)
        self.canvas.config(scrollregion=(0, 0, self.content_w, self.total_h))
        self.canvas.delete("all")
        self.drawn.clear()
        self.cache.clear()

        if anchor:
            p, frac, xfrac = anchor
            self.canvas.yview_moveto((self.offsets[p] + frac * self.heights[p]) / self.total_h)
            self.canvas.xview_moveto(xfrac)
        if thumbs:
            self.layout_thumbs()
        self.update_view()

    def update_view(self):
        """Draw the pages that are on screen (plus a margin) and remove the rest."""
        if not self.doc or not self.offsets:
            return
        _, ch = self.canvas_size()
        top = self.canvas.canvasy(0)
        bottom = top + ch
        margin = ch * 0.5
        i = max(0, bisect.bisect_right(self.offsets, top - margin) - 1)
        visible = []
        while i < len(self.offsets) and self.offsets[i] < bottom + margin:
            visible.append(i)
            i += 1
        for p in list(self.drawn):
            if p not in visible:
                self.canvas.delete(f"pg{p}")
                self.drawn.discard(p)
        for p in visible:
            if p not in self.drawn:
                self.draw_page(p)

        # which page is the reader on?
        cur = max(0, bisect.bisect_right(self.offsets, top + (bottom - top) * 0.35) - 1)
        if self.pending is not None:
            q = self.pending
            if self.offsets[q] < bottom and self.offsets[q] + self.heights[q] > top:
                cur = q
            else:
                self.pending = None
        if cur != self.page_no:
            self.page_no = cur
            self.highlight_thumb()
        self.update_status()

    def page_image(self, p):
        if p in self.cache:
            self.cache.move_to_end(p)
            return self.cache[p]
        pix = self.prepare(p).get_pixmap(matrix=fitz.Matrix(self.zoom, self.zoom), alpha=False)
        photo = ImageTk.PhotoImage(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
        self.cache[p] = photo
        for key in list(self.cache):                              # keep the cache small
            if len(self.cache) <= CACHE_PAGES:
                break
            if key not in self.drawn and key != p:
                del self.cache[key]
        return photo

    def draw_page(self, p):
        c, tag = self.canvas, f"pg{p}"
        x, y, w, h = (self.content_w - self.widths[p]) / 2, self.offsets[p], self.widths[p], self.heights[p]
        c.create_rectangle(x + 4, y + 4, x + w + 4, y + h + 4, fill="#444", outline="", tags=tag)
        c.create_rectangle(x, y, x + w, y + h, fill="white", outline="", tags=tag)
        c.create_image(x, y, anchor="nw", image=self.page_image(p), tags=tag)
        if p in self.hits_by_page:                                # search highlights
            mat = self.doc[p].rotation_matrix
            for idx, rect in self.hits_by_page[p]:
                r = rect * mat
                c.create_rectangle(x + r.x0 * self.zoom, y + r.y0 * self.zoom,
                                   x + r.x1 * self.zoom, y + r.y1 * self.zoom,
                                   outline="red" if idx == self.hit_idx else "orange", width=2, tags=tag)
        self.drawn.add(p)

    def refresh_pages(self):
        for p in list(self.drawn):
            self.canvas.delete(f"pg{p}")
        self.drawn.clear()
        self.update_view()

    def on_yscroll(self, first, last):
        self.vs.set(first, last)
        if self.view_job is None:
            self.view_job = self.root.after_idle(self.run_view_update)

    def run_view_update(self):
        self.view_job = None
        self.update_view()

    def on_resize(self, event):
        if self.doc:
            if self.resize_job:
                self.root.after_cancel(self.resize_job)
            self.resize_job = self.root.after(120, self.relayout)

    def on_drag(self, event):
        self.pending = None
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    # ------------------------------------------------------------ thumbnails
    def layout_thumbs(self):
        self.thumb_offsets, self.thumb_heights, y = [], [], THUMB_PAD
        for i in range(self.page_count()):
            w, h = self.eff_size(i)
            th = THUMB_W * h / w
            self.thumb_offsets.append(y)
            self.thumb_heights.append(th)
            y += th + THUMB_LABEL + THUMB_PAD
        self.thumb_total = y
        self.tcanvas.config(scrollregion=(0, 0, SIDEBAR_W, y))
        self.tcanvas.delete("all")
        self.thumb_drawn.clear()
        self.update_thumbs()
        self.highlight_thumb()

    def update_thumbs(self):
        if not self.doc or not self.thumb_offsets or not self.sidebar_on.get():
            return
        top = self.tcanvas.canvasy(0)
        bottom = top + max(self.tcanvas.winfo_height(), 200)
        i = max(0, bisect.bisect_right(self.thumb_offsets, top - 200) - 1)
        visible = []
        while i < len(self.thumb_offsets) and self.thumb_offsets[i] < bottom + 200:
            visible.append(i)
            i += 1
        for p in list(self.thumb_drawn):
            if p not in visible:
                self.tcanvas.delete(f"th{p}")
                del self.thumb_drawn[p]
        x0 = (SIDEBAR_W - THUMB_W) // 2
        for p in visible:
            if p in self.thumb_drawn:
                continue
            y, th, tag = self.thumb_offsets[p], self.thumb_heights[p], f"th{p}"
            w = self.eff_size(p)[0]
            pix = self.prepare(p).get_pixmap(matrix=fitz.Matrix(THUMB_W / w, THUMB_W / w), alpha=False)
            photo = ImageTk.PhotoImage(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
            self.thumb_drawn[p] = photo                               # keeps a reference alive
            self.tcanvas.create_rectangle(x0, y, x0 + THUMB_W, y + th, fill="white", outline="", tags=tag)
            self.tcanvas.create_image(x0, y, anchor="nw", image=photo, tags=tag)
            self.tcanvas.create_text(SIDEBAR_W // 2, y + th + THUMB_LABEL / 2, text=str(p + 1),
                                     fill="white", tags=tag)
        self.tcanvas.tag_raise("sel")

    def highlight_thumb(self):
        if not self.doc or not self.thumb_offsets:
            return
        p = self.page_no
        x0, y, th = (SIDEBAR_W - THUMB_W) // 2, self.thumb_offsets[p], self.thumb_heights[p]
        self.tcanvas.delete("sel")
        self.tcanvas.create_rectangle(x0 - 4, y - 4, x0 + THUMB_W + 4, y + th + 4,
                                      outline="#3b82f6", width=3, tags="sel")
        top, height = self.tcanvas.canvasy(0), max(self.tcanvas.winfo_height(), 200)
        if y < top or y + th + THUMB_LABEL > top + height:           # scroll sidebar to the current page
            self.tcanvas.yview_moveto(max(0, y - THUMB_PAD) / self.thumb_total)

    def on_tscroll(self, first, last):
        self.ts.set(first, last)
        if self.thumb_job is None:
            self.thumb_job = self.root.after_idle(self.run_thumb_update)

    def run_thumb_update(self):
        self.thumb_job = None
        self.update_thumbs()
        self.tcanvas.tag_raise("sel")

    def on_thumb_click(self, event):
        if not self.doc:
            return
        y = self.tcanvas.canvasy(event.y)
        i = bisect.bisect_right(self.thumb_offsets, y + THUMB_PAD / 2) - 1
        if 0 <= i < self.page_count():
            self.go_to(i)

    def toggle_sidebar_button(self):
        self.sidebar_on.set(not self.sidebar_on.get())
        self.toggle_sidebar()

    def toggle_sidebar(self):
        if self.sidebar_on.get():
            self.sidebar.grid()
            self.root.update_idletasks()
            self.update_thumbs()
            self.highlight_thumb()
        else:
            self.sidebar.grid_remove()


    def zoom_by(self, factor):
        if not self.doc:
            return
        new = max(MIN_ZOOM, min(MAX_ZOOM, self.zoom * factor))
        if abs(new - self.zoom) < 1e-6:
            return
        self.fit_mode, self.zoom = None, new
        self.relayout()

    def zoom_reset(self):
        if self.doc:
            self.fit_mode, self.zoom = None, 1.0
            self.relayout()

    def set_fit(self, mode):
        if self.doc:
            self.fit_mode = mode
            self.relayout()
            self.go_to(self.page_no)

    def rotate(self):
        if self.doc:
            self.rotation = (self.rotation + 90) % 360
            self.relayout(thumbs=True)


    def go_to(self, n):
        if not self.doc:
            return
        n = max(0, min(self.page_count() - 1, n))
        self.pending = self.page_no = n
        self.canvas.yview_moveto(max(0, self.offsets[n] - PAD) / self.total_h)
        self.update_view()
        self.highlight_thumb()

    def goto_entry(self, event=None):
        try:
            self.go_to(int(self.page_var.get()) - 1)
        except ValueError:
            self.update_status()
        self.canvas.focus_set()

    def scroll_main(self, amount, what):
        if self.doc:
            self.pending = None
            self.canvas.yview_scroll(amount, what)

    def on_wheel(self, event, direction=None):
        if not self.doc:
            return
        if direction is None:
            direction = -1 if event.delta > 0 else 1
        if event.state & 0x4:                                           
            self.zoom_by(ZOOM_STEP if direction < 0 else 1 / ZOOM_STEP)
            return
        try:
            under = self.root.winfo_containing(event.x_root, event.y_root)
        except KeyError:
            under = None
        if under is not None and str(under).startswith(str(self.tcanvas)):
            self.tcanvas.yview_scroll(direction * 3, "units")
        else:
            self.scroll_main(direction * 3, "units")


    def find(self, step=1):
        if not self.doc:
            return
        query = self.search_var.get().strip()
        if not query:
            return
        if query != self.query:                                         
            self.root.config(cursor="watch")
            self.root.update_idletasks()
            self.hits = [(i, r) for i in range(self.page_count()) for r in self.doc[i].search_for(query)]
            self.hits_by_page = {}
            for idx, (pn, rect) in enumerate(self.hits):
                self.hits_by_page.setdefault(pn, []).append((idx, rect))
            self.root.config(cursor="")
            self.query, self.hit_idx, self.match_text = query, -1, ""
            if not self.hits:
                self.refresh_pages()
                messagebox.showinfo("Find", f'"{query}" was not found.')
                return
        self.hit_idx = (self.hit_idx + step) % len(self.hits)
        pn, rect = self.hits[self.hit_idx]
        mat = self.prepare(pn).rotation_matrix
        y = self.offsets[pn] + (rect * mat).y0 * self.zoom
        self.pending = None
        self.canvas.yview_moveto(max(0, y - 100) / self.total_h)
        self.match_text = f'Match {self.hit_idx + 1} of {len(self.hits)} for "{query}"'
        self.refresh_pages()


def main():
    root = tk.Tk()
    if fitz is None or Image is None:
        messagebox.showerror("Missing libraries",
                             "Please install the required libraries first:\n\npip install pymupdf pillow")
        return
    viewer = PDFViewer(root)
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        root.after(150, lambda: viewer.open_pdf(sys.argv[1]))
    root.mainloop()


if __name__ == "__main__":
    main()
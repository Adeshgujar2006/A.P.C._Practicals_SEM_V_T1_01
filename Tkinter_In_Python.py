import difflib
import json
import re
import tkinter as tk
import urllib.request
from tkinter import ttk, messagebox

DATA = {
    "Maharashtra": {

        "Solapur": ["Sangola", "Pandharpur", "Madha", "Malshiras", "Karmala", "Akluj"],
        "Kolhapur": ["Karveer", "Panhala", "Kagal", "Gadhinglaj", "Ajra", "Bhudargad", "GaganBawada"],
        "Yavatmal": ["Yavatmal", "Ner", "Darwha", "Digras", "Pusad", "Pandharkawda", "Wani", "Ralegaon", "Babhulgaon", "Zari", "Arni"],
    },
    "Karnataka": {
        "Belgavi": ["Belagavi", "Athani", "Gokak"],
        "Bengaluru Urban": ["Bengaluru North", "Bengaluru South"],
    },


}


def check_pincode(pin, state, district):

    if not re.fullmatch(r"[1-9][0-9]{5}", pin):
        return "invalid", "Pincode must be 6 digits and cannot start with 0."

    try:
        url = f"https://api.postalpincode.in/pincode/{pin}"
        with urllib.request.urlopen(url, timeout=5) as r:
            result = json.loads(r.read().decode())[0]
    except Exception:
        return "offline", ""  # format is fine, could not verify online

    if result.get("Status") != "Success" or not result.get("PostOffice"):
        return "invalid", "This pincode does not exist."

    offices = result["PostOffice"]
    states = {o["State"].lower() for o in offices}
    districts = {o["District"].lower() for o in offices}
    state_names = ", ".join(sorted({o["State"] for o in offices}))
    district_names = ", ".join(sorted({o["District"] for o in offices}))

    if state.lower() not in states:
        return "mismatch", f"This pincode ({pin}) belongs to {district_names} district, {state_names} state.\nYou selected {district}, {state}."
    
    if not difflib.get_close_matches(district.lower(), districts, n=1, cutoff=0.8):
        return "mismatch", f"Pincode {pin} belongs to {district_names} district.\nBut you selected {district} district."
    return "ok", ""


root = tk.Tk()
root.title("Registration Page")
root.geometry("420x690")

tk.Label(root, text="Registration Page", font=("Arial", 18, "bold")).grid(
    row=0, column=0, columnspan=2, pady=15)


fields = {}
for i, text in enumerate(["Name", "Mobile Number", "Email"], start=1):
    tk.Label(root, text=text, font=("Arial", 11)).grid(row=i, column=0, padx=15, pady=6, sticky="w")
    e = tk.Entry(root, width=30)
    e.grid(row=i, column=1, pady=6)
    fields[text] = e


state_var, district_var, taluka_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
combos = {}
for i, (text, var) in enumerate(
        [("State", state_var), ("District", district_var), ("Taluka", taluka_var)], start=4):
    tk.Label(root, text=text, font=("Arial", 11)).grid(row=i, column=0, padx=15, pady=6, sticky="w")
    cb = ttk.Combobox(root, textvariable=var, state="readonly", width=27)
    cb.grid(row=i, column=1, pady=6)
    combos[text] = cb

combos["State"]["values"] = list(DATA.keys())


def on_state_change(event=None):
    district_var.set("")
    taluka_var.set("")
    combos["Taluka"]["values"] = []
    combos["District"]["values"] = list(DATA[state_var.get()].keys())


def on_district_change(event=None):
    taluka_var.set("")
    combos["Taluka"]["values"] = DATA[state_var.get()][district_var.get()]


combos["State"].bind("<<ComboboxSelected>>", on_state_change)
combos["District"].bind("<<ComboboxSelected>>", on_district_change)

tk.Label(root, text="Address", font=("Arial", 11)).grid(row=7, column=0, padx=15, pady=6, sticky="nw")
address = tk.Text(root, width=23, height=4)
address.grid(row=7, column=1, pady=6)

tk.Label(root, text="Pincode", font=("Arial", 11)).grid(row=8, column=0, padx=15, pady=6, sticky="w")
pincode = tk.Entry(root, width=30)
pincode.grid(row=8, column=1, pady=6)

agree_var = tk.BooleanVar()
agree = tk.Checkbutton(root, text="I agree to the terms and conditions",
                       variable=agree_var, font=("Arial", 10))
agree.grid(row=9, column=0, columnspan=2, padx=15, pady=6, sticky="w")

output = tk.Label(root, text="", justify="left", anchor="w", font=("Arial", 10))
output.grid(row=11, column=0, columnspan=2, padx=15, pady=10, sticky="w")


def submit():
    data = {k: v.get().strip() for k, v in fields.items()}
    data["State"] = state_var.get()
    data["District"] = district_var.get()
    data["Taluka"] = taluka_var.get()
    data["Address"] = address.get("1.0", tk.END).strip()
    data["Pincode"] = pincode.get().strip()

    if not all(data.values()):
        messagebox.showwarning("Missing data", "Please fill in all fields.")
        return
    if not re.fullmatch(r"[6-9]\d{9}", data["Mobile Number"]):
        messagebox.showerror("Invalid mobile", "Mobile number must be 10 digits and start with 6, 7, 8 or 9.")
        return
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", data["Email"]):
        messagebox.showerror("Invalid email", "Please enter a valid email address.")
        return

    if not agree_var.get():
        messagebox.showwarning("Terms", "Please tick the checkbox to agree to the terms.")
        return

    status, msg = check_pincode(data["Pincode"], data["State"], data["District"])
    if status == "invalid":
        messagebox.showerror("Invalid pincode", msg)
        return
    if status == "mismatch":
        messagebox.showwarning("Pincode belongs to another place", msg)
        return
    if status == "offline":
        messagebox.showinfo("Pincode", "Pincode format is valid (no internet, so it was not verified online).")

    output.config(text="\n".join(f"{k}: {v}" for k, v in data.items()))
    messagebox.showinfo("Success", "Registration successful!")


tk.Button(root, text="Submit", width=15, bg="#2d6cdf", fg="white",
          command=submit).grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
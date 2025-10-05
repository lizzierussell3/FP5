import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import re

# -----------------------------
# Database Setup
# -----------------------------
def create_db():
    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            preferred_contact TEXT
        )
    ''')
    conn.commit()
    conn.close()

# -----------------------------
# Submit Function
# -----------------------------
def submit_form():
    name = entry_name.get().strip()
    birthday = entry_birthday.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    address = entry_address.get("1.0", tk.END).strip()
    preferred_contact = contact_method.get()

    # Basic validation
    if not name:
        messagebox.showerror("Validation Error", "Name is required.")
        return
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Validation Error", "Invalid email format.")
        return

    # Insert into database
    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO customers (name, birthday, email, phone, address, preferred_contact)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, birthday, email, phone, address, preferred_contact))
    conn.commit()
    conn.close()

    # Clear form
    clear_form()
    messagebox.showinfo("Success", "Customer information submitted!")

# -----------------------------
# Clear Form Function
# -----------------------------
def clear_form():
    entry_name.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)
    contact_method.set("Email")  # Reset to default

# -----------------------------
# GUI Setup
# -----------------------------
create_db()
root = tk.Tk()
root.title("Customer Information Form")
root.geometry("400x500")
root.resizable(False, False)

# Labels and Fields
tk.Label(root, text="Name *").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Birthday (YYYY-MM-DD)").pack(pady=5)
entry_birthday = tk.Entry(root, width=40)
entry_birthday.pack()

tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Phone Number").pack(pady=5)
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

tk.Label(root, text="Address").pack(pady=5)
entry_address = tk.Text(root, width=30, height=4)
entry_address.pack()

tk.Label(root, text="Preferred Contact Method").pack(pady=5)
contact_method = ttk.Combobox(root, values=["Email", "Phone", "Mail"], state="readonly")
contact_method.set("Email")
contact_method.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white", width=20).pack(pady=20)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Student Form")
root.geometry("300x300")

# Labels
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Submit function
def submit():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    messagebox.showinfo("Form Data",
                        f"Name: {name}\nEmail: {email}\nAge: {age}")

# Button
tk.Button(root, text="Submit", command=submit).pack(pady=10)

# Run app
root.mainloop()
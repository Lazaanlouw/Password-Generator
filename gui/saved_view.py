#Saved_view.py is the Saved Password Screen that handles displaying all saved passwords.
    #This file also holds the functionality of Copying password to clipboard, Deleting a saved password and refreshing screen.

import tkinter as tk
from tkinter import ttk, messagebox
from password_generator import model

#Function to create the saved passwords screen
def create_saved_frame(container):
    frame = tk.Frame(container)

    title_label = tk.Label(frame, text="Saved Passwords", font=("Ariel", 16, "bold"))
    title_label.pack(pady=10)

    tree_container = tk.Frame(frame)
    tree_container.pack(fill="both", expand=True, padx=10, pady=5)
    

    cols = ("#", "password")
    tree = ttk.Treeview(tree_container, columns=cols, show="headings", selectmode="browse", height=10)
    tree.heading("#", text="#")
    tree.heading("password", text="Password")
    tree.column("#", width=40, anchor="center")
    tree.column("password", width=600, anchor="w")

    vsb = ttk.Scrollbar(tree_container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    tree.pack(fill="both", expand=True, side="left")
    vsb.pack(side="right", fill="y")

    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=8)

    #Buttons on the screen (Copy, Delete and Refresh)
    copy_btn = tk.Button(btn_frame, text="Copy Selected", width=15)
    delete_btn = tk.Button(btn_frame, text="Delete Selected", width=15)
    refresh_btn = tk.Button(btn_frame, text="Refresh", width=10)

    copy_btn.grid(row=0, column=0, padx=6)
    delete_btn.grid(row=0, column=1, padx=6)
    refresh_btn.grid(row=0, column=2, padx=6)

    #Function that calls the view password function in model.
    def load_passwords():
        tree.delete(*tree.get_children())
        passwords = model.view_passwords() or []
        for i, p in enumerate(passwords):
            tree.insert("", "end", iid=str(i), values=(i+1, p))

    #Function that allows you to copy the passwords you select.
    def copy_selected():
        sel = tree.selection()
        if not sel:
            messagebox.showinfo("Copy", "Please select a password to copy.")
            return
        iid = sel[0]
        password = tree.item(iid, "values")[1]
        frame.winfo_toplevel().clipboard_clear()
        frame.winfo_toplevel().clipboard_append(password)
        messagebox.showinfo("Copy", "Password copied to clipboard.")

    #Function to delete password from the list of saved passwords.
    def delete_selected():
        sel = tree.selection()
        if not sel:
            messagebox.showinfo("Delete", "Please select a password to delete.")
            return
        iid = sel[0]
        index = int(iid)
        confirm = messagebox.askyesno("Delete", "Delete the selected password?")
        if not confirm:
            return
        success = model.delete_selected_password(index)
        if success:
            messagebox.showinfo("Deleted", "Password deleted.")
            load_passwords()
        else:
            messagebox.showerror("Error", "Failed to delete password.")

    copy_btn.config(command=copy_selected)
    delete_btn.config(command=delete_selected)
    refresh_btn.config(command=load_passwords)
    
    #Reloads the screen when data is changed.
    frame.bind("<<ShowFrame>>", lambda e: load_passwords())

    load_passwords()

    return frame
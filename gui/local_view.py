#local_view.py.
#This file handles the entire local password generation screen.
#Including displaying the strength of the password and option to save the generated password.

import tkinter as tk
from tkinter import messagebox
from password_generator import model
from password_generator.gui.theme import APP_COLORS, APP_FONTS

#Function to create the local password generator screen.
def create_local_frame(container):
    frame = tk.Frame(container, bg=APP_COLORS["bg"])

    #Title.
    local_title_label = tk.Label(frame, text="Password Generator", font=APP_FONTS["title"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"])
    local_title_label.pack(pady=10)

    #Input password length.
    local_length_label = tk.Label(frame, text="Enter password length:", font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"])
    local_length_label.pack()

    local_length_entry = tk.Entry(frame, width=10, font=APP_FONTS["entry"])
    local_length_entry.pack(pady=5)

    #Input boxes for include numbers and symbols.
    local_use_numbers_var = tk.BooleanVar(value=True)
    local_use_symbols_var = tk.BooleanVar(value=True)

    local_numbers_check = tk.Checkbutton(frame, text="Include numbers", variable=local_use_numbers_var,
        font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"],
        selectcolor=APP_COLORS["accent"])
    local_numbers_check.pack()

    local_symbols_check = tk.Checkbutton(frame, text="Include symbols", variable=local_use_symbols_var,
        font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"],
        selectcolor=APP_COLORS["accent"])
    local_symbols_check.pack()

    #password Label.
    local_password_label = tk.Label(frame, text="", font=APP_FONTS["output"],
        bg=APP_COLORS["bg"], fg=APP_COLORS["accent"])
    local_password_label.pack(pady=5)

    #Strength Label.
    local_strength_label = tk.Label(frame, text="", font=APP_FONTS["label"],
        bg=APP_COLORS["bg"])
    local_strength_label.pack()

    def generate_local_password():
        try:
            length = int(local_length_entry.get())
        except ValueError:
            local_password_label.config(text="Enter a valid number")
            return
        
        #Validation so user does not enter more than 25 and less than 7 characters.
        if length < 7:
            local_password_label.config(text="Password must be atleast 7 characters")
            return
        elif length > 25:
            local_password_label.config(text="Password must be at most 25 characters")
            return

        use_numbers = local_use_numbers_var.get()
        use_symbols = local_use_symbols_var.get()
        
        password = model.generate_password(length, use_numbers, use_symbols)
        local_password_label.config(text=password)

        #Getting the password strength from model.py.
        strength = model.password_strength(password)

        #Password Strength Color.
        if strength.lower() == "weak":
            color = "red"
        elif strength.lower() == "medium":
            color = "orange"
        else:
            color = "green"

        local_strength_label.config(text=f" Password Strength: {strength}", fg=color)

    # Buttons
    btn_frame = tk.Frame(frame, bg=APP_COLORS["bg"])
    btn_frame.pack(pady=5)

    #Button to generate password..
    local_generate_button = tk.Button(btn_frame, text="Generate Password", command=generate_local_password)
    local_generate_button.grid(row=0, column=0, padx=5)

    save_local_button = tk.Button(btn_frame, text="Save Password", width=15)
    save_local_button.grid(row=0, column=1, padx=5)

    def save_local_password():
        password = local_password_label.cget("text")
        if not password:
            tk.messagebox.showinfo("Save", "No password to save.")
            return
        model.save_password(password)
        tk.messagebox.showinfo("Save", "Password saved successfully!")

    save_local_button.config(command=save_local_password)

    return frame

import tkinter as tk
from tkinter import messagebox
from password_generator import model
from password_generator.gui.theme import APP_COLORS, APP_FONTS

#Function to create the APi Password Generator Screen.
def create_api_frame(container):
    frame = tk.Frame(container, bg=APP_COLORS["bg"])

    #Title.
    api_title_label = tk.Label(frame, text=" API Password Generator", font=APP_FONTS["title"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"])
    api_title_label.pack(pady=10)

    #Input password length.
    api_length_label = tk.Label(frame, text="Enter password length:", font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"])
    api_length_label.pack(pady=5)

    api_length_entry = tk.Entry(frame, width=10, font=APP_FONTS["entry"])
    api_length_entry.pack(pady=5)

    #Input boxes for include numbers and symbols.
    api_use_numbers_var = tk.BooleanVar(value=True)
    api_use_symbols_var = tk.BooleanVar(value=True)
    api_use_upper_var = tk.BooleanVar(value=True)
    api_use_lower_var = tk.BooleanVar(value=True)

    api_numbers_check = tk.Checkbutton(frame, text="Include numbers", variable=api_use_numbers_var, font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"],
        selectcolor=APP_COLORS["accent"])
    api_numbers_check.pack()

    api_symbols_check = tk.Checkbutton(frame, text="Include symbols", variable=api_use_symbols_var, font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"],
        selectcolor=APP_COLORS["accent"])
    api_symbols_check.pack()
    
    api_upper_check = tk.Checkbutton(frame, text="Include UpperCase", variable=api_use_upper_var, font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"],
        selectcolor=APP_COLORS["accent"])
    api_upper_check.pack()

    api_lower_check = tk.Checkbutton(frame, text="Include lowerCase", variable=api_use_lower_var, font=APP_FONTS["label"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"],
        selectcolor=APP_COLORS["accent"])
    api_lower_check.pack()

    #password Label.
    api_password_label = tk.Label(frame, text="", font=APP_FONTS["password"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"])
    api_password_label.pack(pady=5)

    #Strength Label
    api_strength_label = tk.Label(frame, text="", font=APP_FONTS["strength"], bg=APP_COLORS["bg"], fg=APP_COLORS["fg"])
    api_strength_label.pack(pady=5)

    #Function that generates the API password with error handling.
    def generate_api_password():
        try:
            length = int(api_length_entry.get())
        except ValueError:
            api_password_label.config(text="Enter a valid number")
            return
        
        #Validation so user does not enter more than 25 and less than 7 characters.
        if length < 7:
            api_password_label.config(text="Password must be atleast 7 characters")
            return
        elif length > 25:
            api_password_label.config(text="Password must be at most 25 characters")
            return

        use_numbers = api_use_numbers_var.get()
        use_symbols = api_use_symbols_var.get()
        use_upper = api_use_upper_var.get()
        use_lower = api_use_lower_var.get()

        password = model.api_password(length=length, numbers=1, special=1, upper=1, lower=1)
        
        password = model.filter_password(password,
            numbers=use_numbers,
            special=use_symbols,
            upper=use_upper,
            lower=use_lower   
        )
        api_password_label.config(text=password)

        #Getting the password strength from model.py.
        strength = model.password_strength(password)

        #Password Strength Color.
        if strength.lower() == "weak":
            color = "red"
        elif strength.lower() == "medium":
            color = "orange"
        else:
            color = "green"

        api_strength_label.config(text=f" Password Strength: {strength}", fg=color)

    # Buttons
    btn_frame = tk.Frame(frame, bg=APP_COLORS["bg"])
    btn_frame.pack(pady=5)

    #Button to generate password.
    api_generate_button = tk.Button(btn_frame, text="Generate Password", command=generate_api_password)
    api_generate_button.grid(row=0, column=0, padx=5)

    #Button to save API generated password.
    save_api_button = tk.Button(btn_frame, text="Save Password", width=15)
    save_api_button.grid(row=0, column=1, padx=5)

    #Function that calls the save password function in model.
    def save_api_password():
        password = api_password_label.cget("text")
        if not password:
            tk.meassagebox.showinfo("Save", "No password to save.")
            return
        model.save_password(password)
        tk.messagebox.showinfo("Save", "Password saved successfully!")

    save_api_button.config(command=save_api_password)
    
    return frame

#gui.py
#Main application window setup for the Password Generator.
#Handles navigation between Local, API, and Saved Password views.


import tkinter as tk
from password_generator import model
from password_generator.gui.local_view import create_local_frame
from password_generator.gui.api_view import create_api_frame
from password_generator.gui.saved_view import create_saved_frame
from password_generator.gui.theme import APP_COLORS, APP_FONTS

def show_frame(name):
    frame = frames[name]
    frame.tkraise()
    frame.event_generate("<<ShowFrame>>")

#Main window.
root = tk.Tk()
root.configure(bg=APP_COLORS["bg"])
root.title("Password Generator")
root.geometry("800x400")
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Menu Bar.
menu_bar = tk.Menu(root, bg=APP_COLORS["accent"], fg=APP_COLORS["fg"], font=APP_FONTS["menu"])
root.config(menu=menu_bar)

#File Menu.
file_menu = tk.Menu(menu_bar, tearoff=0, bg=APP_COLORS["bg"], fg=APP_COLORS["fg"], font=APP_FONTS["menu"])
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

#View Menu.
view_menu = tk.Menu(menu_bar, tearoff=0, bg=APP_COLORS["bg"], fg=APP_COLORS["fg"], font=APP_FONTS["menu"])
menu_bar.add_cascade(label="View", menu=view_menu)

#Main container.
container = tk.Frame(root, bg=APP_COLORS["bg"])
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

frames = {}

frames["local"] = create_local_frame(container)
frames["api"] = create_api_frame(container)
frames["saved"] = create_saved_frame(container)


for frame in frames.values():
    frame.grid(row=0, column=0, sticky="nsew")

view_menu.add_command(label="Local Generator", command=lambda: show_frame("local"))
view_menu.add_command(label="API Generator", command=lambda: show_frame("api"))
view_menu.add_command(label="Saved Passwords", command=lambda: show_frame("saved"))

#Default view when the Application starts.
show_frame("local")

#Run App.
root.mainloop()

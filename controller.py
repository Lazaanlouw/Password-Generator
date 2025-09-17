from . import model
from . import view

def handle_generate():
    length = view.ask_length()
    use_numbers = view.prompt_yes_no("Would you like your password to have numbers (y/n): ")
    use_symbols = view.prompt_yes_no("Would you like your password to have symbols (y/n): ")
    save = view.prompt_yes_no("Would you like to save your password (y/n): ")

    #generating password and strength
    password = model.generate_password(length, use_numbers, use_symbols)
    strength = model.password_strength(password)

    #showing password and strength after generated
    view.show_password_strength(password, strength)

    if view.prompt_yes_no("Copy password to clipboard? (y/n): "):
        view.copy_to_clipboard(password)

    if save:
        model.save_password(password)
        view.display_message("Password saved to passwords.txt")
#Fetching and showing all saved passwords
def handle_view():
    passwords = model.view_passwords()
    view.show_saved_passwords(passwords)

#The Main section(Handles the process of the system)
def main():
    while True:
        view.display_menu()
        choice = view.user_menu_choice()

        if choice == "1":
            handle_generate()
        elif choice == "2":
            handle_view()
        elif choice == "3":
            passwords = model.view_passwords()
            if not passwords:
                view.show_saved_passwords(passwords)
                continue
            index = view.user_password_delete(passwords)
            success = model.delete_selected_password(index)
            if success:
                print("Password Deleted Successful.")
            else:
                print("Failed to delete password")
        elif choice == "4":
            view.display_message("Goodbye Crazy Boy")
            break
        else:
            view.display_message(f"'{choice}' is an invalid option, please try again.")

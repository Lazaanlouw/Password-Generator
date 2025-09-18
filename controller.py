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

def api_generate():
    length = view.ask_length()
    use_numbers = view.prompt_yes_no("Should your password include Numbers (y/n)? ")
    use_symbols = view.prompt_yes_no("Should your password include Symbols (y/n) ")
    use_upper = view.prompt_yes_no("Should your password include Uppercase Letters (y/n) ")
    use_lower = view.prompt_yes_no("Should your password include Lowercase Letters (y/n) ")
    save = view.prompt_yes_no("Would you like to save your password (y/n): ")

    password = model.api_password(
        length=length,
        upper=str(use_upper).lower(),
        lower=str(use_lower).lower(),
        numbers=str(use_numbers).lower(),
        special=str(use_symbols).lower()
    )
    password = model.filter_password(password, use_upper, use_lower , use_numbers, use_symbols)

    if password:
        print("\nPassword from API:", password)
    else:
        print("Failed to fetch password")

    if save:
        model.save_password(password)
        view.display_message("Password saved to passwords.txt")

    if view.prompt_yes_no("Copy password to clipboard? (y/n): "):
        view.copy_to_clipboard(password)

    strength = model.password_strength(password)
    view.show_password_strength(password, strength)

#The Main section(Handles the process of the system)
def main():
    while True:
        view.display_menu()
        choice = view.user_menu_choice()

        if choice == "1":
            handle_generate()
        elif choice == "2":
            api_generate() 
        elif choice == "3":
            handle_view()
        elif choice == "4":
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
        elif choice == "5":
            view.display_message("Goodbye Crazy Boy")
            break
        else:
            view.display_message(f"'{choice}' is an invalid option, please try again.")

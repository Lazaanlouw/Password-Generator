import pyperclip # pyright: ignore[reportMissingModuleSource]

#User Interface input and output functions 

#displaying the menu.
def display_menu():
    print("\n--- Password Generator Menu ---")
    print("1. Generate Password")
    print("2. Generate Password with API")
    print("3. View Saved Passwords")
    print("4. Delete a Password")
    print("5. Exit")

#Getting the choice made by the user at the menu.
def user_menu_choice():
    return input("Choose an option (1/2/3/4/5): ").strip()

#Getting the length of the password being created with error handling.
def ask_length():
    while True:
        try:
            value = int(input("Enter the length of the password you would like: "))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid Number.")

#Asking the user yes or no questions base on numbers, symbols and if they want to save password.
def prompt_yes_no(prompt: str):
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "yes"):
            return False
        print("Invalid input. Please type 'y' or 'n'.")

#Displaying the generated password.
def show_generated_password(password: str):
    print("\nYour generated password is:", password, "\n")

#Displaying all saved passwords
def show_saved_passwords(passwords: list):
    if not passwords:
        print("\nNo saved passwords found.\n")
        return
    print("\nSaved passwords:")
    for i, p in enumerate(passwords, 1):
        print(f"{i}. {p}")
    print()

#Displaying saved passwords and then prompts user to choose hwich password to delete.
def user_password_delete(passwords: list):
    print("\nSaved Passwords:")
    for i, p in enumerate(passwords, 1):
        print(f"{i}. {p}")

    while True:
        choice = input("Enter the number of the password to delete: ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        choice = int(choice)
        if 1 <= choice <= len(passwords):
            return choice - 1
        else:
            print(f"Please choose a number between 1 and {len(passwords)}.")

#Display messages
def display_message(message: str):
    print(message)

#Displays generated password and its strenngth
def show_password_strength(password: str, strength: str):
    print(f"\nPassword: {password}")
    print(f"Strength: {strength}\n")

#Displays password was copied to clipboard
def copy_to_clipboard(password: str):
    pyperclip.copy(password)
    print("Password copied to clipboard!\n")

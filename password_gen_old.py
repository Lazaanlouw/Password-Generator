#Importing Random characters and Strings like letters,numbers etc.
import random
import string

def generate_password(length, use_numbers, use_symbols):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    characters = letters

    if use_numbers:
        characters += digits
    if use_symbols:
        characters += punctuation

    if not use_numbers and not use_symbols:
         print("NOTE: Only letters will be used")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
          
def ask_length():

    while True:
                try:
                    length = int(input("Enter the length of the password you would like: "))
                    if length > 0:
                        return length
                    print("Please enter a positive number.")
                except ValueError:
                    print("Please enter a valid number.")

def ask_yes_no(prompt):
    while True:
         answer = input(prompt).strip().lower()
         if answer in ("y", "n", "yes", "no"):
              return (answer == "y" or answer == "yes")
         print("Invalid input. Please type 'y' or 'n'.")

def save_password(password):
     with open("passwords.txt", "a") as file:
          file.write(password + "\n")

def view_password():
    try:
          with open("passwords.txt", "r")as file:
               for line in file:
                    print(line.strip())
    except FileNotFoundError:
        print("No Saved passwords found")
          
def ask_save_password(prompt):
     return ask_yes_no(prompt)

def main():

    while True:
        print("\n--- Password Generator Menu ---")
        print("1. Generate Password")
        print("2. View Saved Passwords")
        print("3. Exit")

        userChoice = input("Choose an Option (1/2/3): ").strip()

        if userChoice == "1":

            # Ask for length
            length = ask_length()


            # Ask for numbers and symbols
            use_numbers = ask_yes_no("Would you like your password to have numbers (y/n): ")
            use_symbols = ask_yes_no("Would you like your password to have symbols (y/n): ")
            use_save_password = ask_save_password("Would you like to save your password (y/n): ")
            

            #Generates and prints password
            password = generate_password(length, use_numbers, use_symbols)
            print("\nYour generated Password is:", password, "\n")
            if use_save_password:
                 save_password(password)

        elif userChoice == "2":
                view_password() 

        elif userChoice == "3":
            print("Goodbye User!!!")
            break

        else:
            print(f"'{userChoice}' is an invalid option, please choose 1, 2 or 3.")

if __name__ == "__main__":
    main()
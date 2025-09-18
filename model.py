#Data and logic: Password Generation and File I/O.

#Importing Random characters and Strings like letters,numbers etc.
import random
import string
import requests# pyright: ignore[reportMissingModuleSource]



def generate_password(length, use_numbers, use_symbols):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    characters = letters

    #Code that joins the letters to the numbers and symbols
    if use_numbers:
        characters += digits
    if use_symbols:
        characters += punctuation

    #If numbers and symbols are not selected, only letters will be added.
    if not use_numbers and not use_symbols:
         print("NOTE: Only letters will be used")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Saving password to a .txt file
def save_password(password):
     with open("passwords.txt", "a") as file:
          file.write(password + "\n")

#viewing the .txt file with error handling
def view_passwords():
    try:
          with open("passwords.txt", "r")as file:
               passwords = [line.strip() for line in file]
               return passwords
    except FileNotFoundError:
        return []
    
#Deleting the selected password    
def delete_selected_password(index: int):
     passwords = view_passwords()
     if index < 0 or index >= len(passwords):
          return False
     passwords.pop(index)
     with open("passwords.txt", "w") as file:
        for p in passwords:
            file.write(p + "\n")
     return True

def password_strength(password: str):
     has_letter = False
     has_number = False
     has_symbol = False

#Checking Character types
     for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        else:
            has_symbol = True
#Checking if password is weak, medium or strong. Default is Medium.
     length = len(password)

     if length < 8 or (has_letter and not (has_number or has_symbol)):
         return "Weak"
     elif length <= 12 and ((has_letter and has_number) or (has_letter and has_symbol)):
         return "Medium"
     elif length > 12 and has_letter and has_number and has_symbol:
         return "Strong"
     else:
         return "Medium"

    
def api_password(length=12, upper=True, lower=True, numbers=True, special=True):
    url =  "https://passwordwolf.com/api/"
    params = {
        "length": length,
        "upper": upper,
        "lower": lower,
        "numbers": numbers,
        "special": special,
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data[0]["password"]
        return None
    except Exception as e:
        print("Error fetching password:", e)
        return None
    
def filter_password(password, upper, lower, numbers, special):
    allowed_chars = ""
    if upper:
        allowed_chars += string.ascii_uppercase
    if lower:
        allowed_chars += string.ascii_lowercase
    if numbers:
        allowed_chars += string.digits
    if special:
        allowed_chars += string.punctuation


    filtered = ''.join(c for c in password if c in allowed_chars)

    while len(filtered) < len(password):
        filtered += random.choice(allowed_chars)

    return filtered
#PGEN Simple Password Generator
#Version: 1.0
#Author: Peter Mazela
#Contact: info@elix-it.de
"""Generator for strong passwords (console module)"""
import random

ASCII_LETTERS = 'AaBbCcDdEeFfGgHJKkLMmNnPpQqRrSsTtVvWwXxYyZz'
DIGITS = '123456789'
SPECIAL_CHAR = '!"§$%&/()=?#+-_.:,;<>~*[]{}'

def generate_password(password_length=10, letters=False, digits=False, special=False):
    """Generating strong random passwords using
       ASCII_LETTERS, DIGITS and SPECIAL_CHAR.
       int for password length. default  len of
       10 characters.
    """
    characters = ""
    if letters:
        characters += ASCII_LETTERS
    if digits:
        characters += DIGITS
    if special:
        characters += SPECIAL_CHAR

    if not characters:
        characters = ASCII_LETTERS + DIGITS + SPECIAL_CHAR
    return "".join(random.choices(characters, k=password_length))

def main():
    """Generate Password on module start"""
    try:
        password_length = int(input("# Password length: "))
        if password_length != 0:
            print(generate_password(password_length))

    except ValueError:
        print("Input must be INTEGER, using default Values")
        print(generate_password())


if __name__ == "__main__":
    main()

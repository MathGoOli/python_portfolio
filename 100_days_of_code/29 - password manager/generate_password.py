import random

def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 3
    nr_symbols = 3
    nr_numbers = 3

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    password_letter = ""
    password_number = ""
    password_symbol = ""

    for numloopletter in range(1, nr_letters + 1):
        password_letter += random.choice(letters)
        password_letter += " "
    for numloopnumber in range(1, nr_numbers + 1):
        password_number += random.choice(numbers)
        password_number += " "
    for numloopsymbols in range(1, nr_symbols + 1):
        password_symbol += random.choice(symbols)
        password_symbol += " "
    password = (password_letter + password_number + password_symbol).split()

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    final_password = ""

    random.shuffle(password)

    for numpass in password:
        final_password += numpass
    return final_password





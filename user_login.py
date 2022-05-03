import secrets
import string

alphabet = string.ascii_letters
numbers = string.digits
alpha_numbers = numbers+alphabet

def password_generator():
    while True:
        try:
            password_length = int(input("How long do you want your password to be?"))
        except ValueError:
            print("That is not a (whole) number. Try again")
            continue
        else:
            if password_length > 20:
                print("You don't need a password that long. Come on. Choose one that is between 10 and 20 characters long.")
                continue
            elif password_length < 10:
                print("Choose a password longer than that. Choose one that is between 10 and 20 characters long.")
                continue
            break

    user_password = ""
    for number in range(password_length):
        user_password+= secrets.choice(alpha_numbers)

    return user_password

def user_name(): 
    while True:
        users_name = input("Enter your username:")
        while True:
            user_choice = input(f"Are you sure you want your username to be {users_name}? Choose yes or no to continue.")
            proper_user_choice = user_choice.lower()
            if proper_user_choice == "yes" or proper_user_choice == "no":
                break
            else:
                print("Choose 'yes' or 'no'.")
                continue
        if proper_user_choice == "yes":
            break
        elif proper_user_choice == "no":
            continue
    return users_name[0].upper()+users_name[1:].lower()

def login_page():
    print(f'Hey {user_name()}, your password is {password_generator()}. Remember it for later use!')

login_page()


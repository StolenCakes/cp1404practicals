"""
CP1404/CP5632 - Practical
Program for password conversion into stars

Write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
"""
MINIMUM_PASSWORD_COUNT = 6
MAXIMUM_PASSWORD_COUNT = 12

def main():
    """Function docstring"""
    letter_count = get_password()
    print(letter_count * "*")

def get_password():
    """Check for a valid password"""
    user_password = input("Enter password: ")
    letter_count = len(user_password) # Counts letters in password entered
    while letter_count < MINIMUM_PASSWORD_COUNT or letter_count > MAXIMUM_PASSWORD_COUNT:
        print("Invalid score")
        user_password = input("Enter password: ")
        letter_count = len(user_password)
    return letter_count

main()
"""
CP1404/CP5632 - Practical
Program for score menu with various options

Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions.

In main(), before the menu loop, get a valid score using your function.
When the user quits, say some kind of "farewell".
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

def main():
    global user_score
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            user_score = float(input("Enter your score: "))
            get_valid_score()
        elif choice == "P":
            user_result = get_result(user_score)
            print(f"Result: {user_result}")
        elif choice == "S":
            show_stars(user_score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye!")

def get_valid_score():
    """Get a valid score (must be 0-100 inclusive) from the user."""
    if MINIMUM_SCORE <= user_score <= MAXIMUM_SCORE:
        return user_score
    else:
        print("Invalid score. Please enter a score between 0 and 100 inclusive.")

def get_result(user_score):
    """Return the result based on the given score."""
    if user_score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif user_score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

def show_stars(user_score):
    """Print as many stars as the score."""
    print("*" * int(user_score))

if __name__ == '__main__':
    main()

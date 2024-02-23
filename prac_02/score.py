"""
CP1404/CP5632 - Practical
Copy broken_score.py from prac 1 and rename it to score.py, then commit.

Your main function should ask the user for their score and print the result.
Write a new function that takes in the user's score as a parameter and returns the result to be printed.
Follow SRP: The function should not print it.

Now add a new part to the bottom of your main function that generates a random score and prints the result.
You do NOT need to write a different function to determine the result for the random score.
If you've written your new function properly, you can use it.
If you've breached SRP, then you'll see that you can't.
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

def main():
    user_score = float(input("Enter your score: "))
    user_result = get_result(user_score)
    print(f"Your result: {user_result}")

def get_result(user_score):
    """Return the result based on the given score."""
    if MINIMUM_SCORE <= user_score <= MAXIMUM_SCORE:
        if user_score >= EXCELLENT_THRESHOLD:
            return "Excellent"
        elif user_score >= PASS_THRESHOLD:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid score"

if __name__ == '__main__':
    main()

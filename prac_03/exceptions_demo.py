"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# 1. A ValueError will occur when
# 2. A ZeroDivisionError will occur when the user tries to divide a value by 0. A division by zero is undefined in mathematics, and therefore is automatically marked as an error by Python.
# 3. I've added a while loop that forces a user to reenter the denominator if it's a 0. This will prevent such an error as it would render it impossible for the user to divide the numerator by 0.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero! Please check your values!")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")



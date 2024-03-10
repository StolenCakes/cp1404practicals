"""
CP1404/CP5632 Practical
Program to get numbers and display information about them.
"""

def get_number():
    return int(input("Number: "))

numbers = []

for _ in range(5):
    numbers.append(get_number())

print(f"The first number is {numbers[0]:d}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

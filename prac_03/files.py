"""
CP1404/CP5632 - Practical

1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.

2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).

3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.

4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
"""

NAME_OUTPUT_FILE = "name.txt"
NUMBER_OUTPUT_FILE = "numbers.txt"

# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.
with open(NAME_OUTPUT_FILE, 'w') as out_file:
    user_name = input("Enter your name: ")
    out_file.write(f"{user_name}\n")

# 2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above) then prints, "Your name is Bob" (or whatever the name is in the file).
with open(NAME_OUTPUT_FILE) as in_file:
    read_name = in_file.readline().strip()
    print(f"Your name is {read_name}")

# 3. Write code that opens "numbers.txt", reads only the first two numbers, and adds them together then prints the result, which should be... 59.
with open(NUMBER_OUTPUT_FILE) as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    number_result = first_number + second_number
    print(f"The sum of the first two numbers is: {number_result}")

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
number_total = 0

with open(NUMBER_OUTPUT_FILE) as numbers_file:
    for line in numbers_file:
        number_for_total = int(line.strip())
        number_total += number_for_total

print(f"The total of all numbers is: {number_total}")
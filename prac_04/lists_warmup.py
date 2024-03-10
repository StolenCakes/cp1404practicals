"""
CP1404/CP5632 - Practical
Practice running things in lists
Notes:
The list always starts at [0]
For [x:y], [ ] brackets will appear
[x:] will omit the first x values, [:x] will omit the last x values
[-x] for both of the above cases does the opposite causing the values to appear instead
For [-x], the number will start from the back of the list
Unless specified, the values in the list will not change its type (e.g. "3" will turn out as False, but not 3)
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] # Answer: 3

numbers[-1]  # Answer: 2

numbers[3]  # Answer: 1

numbers[:-1] # Answer: [3, 1, 4, 1, 5, 9]

numbers[3:4]  # Answer: [1]

5 in numbers  # Answer: True

7 in numbers  # Answer: False

"3" in numbers  # Answer: False

numbers + [6, 5, 3]  # Answer: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
numbers [2:]

# Print whether 9 is an element of numbers
9 in numbers
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting

This is a program that uses a 'constant' dictionary to store the Australian state abbreviations and names
e.g., QLD is Queensland
It asks the user for their 'short' state and prints the full state name by looking it up in the dictionary.

Change the program so lowercase inputs also work to show the state names. (There are two places to add a string method.)

Write a loop that prints all the states and names neatly lined up with string formatting, like:

NSW is New South Wales
QLD is Queensland
NT  is Northern Territory

This code uses the "Look Before You Leap" (LBYL) approach to checking if the key is in the dictionary.
Change this to use exceptions and the "Easier to Ask Forgiveness than Permission" (EAFP) approach.
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()  # Converts all input to uppercase in the program so that it works
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")  # Converted to display in string formatting
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
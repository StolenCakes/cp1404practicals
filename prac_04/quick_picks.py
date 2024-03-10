"""
CP1404/CP5632 Practical
Program for a  Lottery Ticket Generator

Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.

"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6

def main():
    """Program to get wanted number of quick picks"""
    quick_pick_count = int(input("How many quick picks? "))
    display_quick_picks(quick_pick_count)

def generate_quick_pick():
    """Function to generate a single quick pick"""
    quick_pick = []
    for i in range(NUMBERS_PER_QUICK_PICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    return sorted(quick_pick)

def display_quick_picks(quick_pick_count):
    """Function to display quick picks"""
    for i in range(quick_pick_count):
        quick_pick = generate_quick_pick()
        print(quick_pick)

main()
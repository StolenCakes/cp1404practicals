"""
CP1404/CP5632 - Practical
Broken program to determine score status
The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

score = float(input("Enter score: "))
while MINIMUM_SCORE <= score <= MAXIMUM_SCORE:
    if score >= EXCELLENT_THRESHOLD:
        print("Excellent")
    elif score >= PASS_THRESHOLD:
        print("Passable")
    else:
        print("Bad")
    score = float(input("Enter score: "))
print("Invalid score")

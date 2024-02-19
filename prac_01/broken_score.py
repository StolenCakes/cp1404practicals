"""
CP1404/CP5632 - Practical
Broken program to determine score status
The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.
"""
MINIMUMSCORE = 0
MAXIMUMSCORE = 100
EXCELLENTTHRESHOLD = 90
PASSTHRESHOLD = 50

score = float(input("Enter score: "))
while MINIMUMSCORE <= score <= MAXIMUMSCORE:
    if score >= EXCELLENTTHRESHOLD:
        print("Excellent")
    elif score >= PASSTHRESHOLD:
        print("Passable")
    else:
        print("Bad")
    score = float(input("Enter score: "))
print("Invalid score")

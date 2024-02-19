"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:
get sales
while sales >= 0
    calculate bonus
    print bonus
    get sales
do next thing
"""
TARGETTHRESHOLD = 1000
BELOWTHRESHOLDBONUS = 0.1
METTHRESHOLDBONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < TARGETTHRESHOLD:
        belowtargetbonus = sales * BELOWTHRESHOLDBONUS  # If sales are under $1,000, the user gets a 10% bonus
        print(f"With your sales of ${sales}, your bonus is: ${belowtargetbonus:.2f}.")
        sales = float(input("Enter sales: $"))
    elif sales >= TARGETTHRESHOLD:
        mettargetbonus = sales * METTHRESHOLDBONUS  # If sales are $1,000 or over, the bonus is 15%
        print(f"With your sales of ${sales}, your bonus is: ${mettargetbonus:.2f}.")
        sales = float(input("Enter sales: $"))
    else:
        print("Invalid amount.")
        sales = float(input("Enter sales: $"))

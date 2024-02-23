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
TARGET_THRESHOLD = 1000
BELOW_THRESHOLD_BONUS = 0.1
MET_THRESHOLD_BONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < TARGET_THRESHOLD:
        below_target_bonus = sales * BELOW_THRESHOLD_BONUS  # If sales are under $1,000, the user gets a 10% bonus
        print(f"With your sales of ${sales}, your bonus is: ${below_target_bonus:.2f}.")
        sales = float(input("Enter sales: $"))
    elif sales >= TARGET_THRESHOLD:
        met_target_bonus = sales * MET_THRESHOLD_BONUS  # If sales are $1,000 or over, the bonus is 15%
        print(f"With your sales of ${sales}, your bonus is: ${met_target_bonus:.2f}.")
        sales = float(input("Enter sales: $"))
    else:
        print("Invalid amount.")
        sales = float(input("Enter sales: $"))

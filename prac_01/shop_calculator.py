"""
CP1404/CP5632 - Practical
Program for a shop calculator

A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

+ Error checking (input validation loop)
After you have completed the above program...
If the number of items is less than zero, the message "Invalid number of items!" should be displayed and this quantity must be re-entered by the user until it is valid.

Sample output:
The output should look something like below (bold text represents user input).
This uses string formatting to set the currency to 2 decimal places.

Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92

Pseudocode:
get number of items, price of items
print total price

if total price > 100
discounted price = total price * 0.9 (10% discount)
print discounted price
"""

DISCOUNT_THRESHOLD = 100
DISCOUNT_CALCULATION = 0.9
STARTING_PRICE = 0
ITEM_THRESHOLD = 0

item_amount = int(input("Number of items: "))
total_price = 0

while item_amount < ITEM_THRESHOLD:
    print("Invalid number of items!")
    item_amount = int(input("Number of items: "))
    total_price = STARTING_PRICE

for i in range(1, item_amount + 1):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    discounted_price = total_price * DISCOUNT_CALCULATION # 10% discount
    print(f"Total price for {item_amount} items is ${discounted_price:.2f}")

else:
    print(f"Total price for {item_amount} items is ${total_price:.2f}")

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MAX_BOUNS = 0.15
MIN_BOUNS = 0.1
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * MAX_BOUNS
    else:
        bonus = sales * MIN_BOUNS
    print(f"Bonus is: {bonus}$")
    sales = float(input("Enter sales: $"))

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

HIGHER_BONUS = 0.15
LOWER_BONUS = 0.1

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * HIGHER_BONUS
    else:
        bonus = sales * LOWER_BONUS
    print(f'Your bonus is {bonus}')
    sales = float(input("Enter sales: $"))

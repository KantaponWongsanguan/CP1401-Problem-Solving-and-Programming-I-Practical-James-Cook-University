
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# sales = float(input("Enter sales: $"))
# if sales >= 1000:
#     bonus = sales * 15 / 100
# else:
#     bonus = sales * 10 / 100
# print(f"{bonus:.0f}")

BONUS_HIGH_SALE = 0.15
BONUS_DEFAULT = 0.10
BONUS_ATTAINABLE = 1000
sales = float(input("Enter sales: $"))  # loop part
while sales >= 0:
    if sales >= BONUS_ATTAINABLE:
        bonus = sales * BONUS_HIGH_SALE  # 15%
    else:
        bonus = sales * BONUS_DEFAULT  # 10%
    print(f"{bonus:.0f}")
    sales = float(input("Enter sales: $"))
print('Thank you.')


DISCOUNT = 0.10  # 10% discount
DISCOUNTABLE_TOTAL_PRICE = 100
total_price = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:  # error checking
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items, 1):
    price_of_items = float(input("Price of item: "))
    while price_of_items < 0:
        print("Invalid price (Price has to be greater than 0)")
        price_of_items = float(input("Price of item: "))
    total_price += price_of_items
if total_price > DISCOUNTABLE_TOTAL_PRICE:
    total_price -= total_price * DISCOUNT

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

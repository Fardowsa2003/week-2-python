# Simple Bill Calculator
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

total = price * quantity

item_word = "item" if quantity == 1 else "items"
print(f"\n{quantity} {item_word} at {price:.2f} each = {total:.2f}")

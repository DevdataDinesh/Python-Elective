print("Enter the items in the stock and their quantities (in the format 'item:quantity'), or 'done' to finish:")
stock = {}
while True:
    item_input = input()
    if item_input == 'done':
        break
    item, quantity = item_input.split(':')
    stock[item] = int(quantity)
print("\nEnter the prices of the items (in the format 'item:price'), or 'done' to finish:")
price = {}
while True:
    item_input = input()
    if item_input == 'done':
        break
    item, price_input = item_input.split(':')
    price[item] = float(price_input)
print("\nAvailable items:")
for item, quantity in stock.items():
    print(f"{item}: {quantity}")

print("\nEnter the items you want to buy (in the format 'item:quantity') or 'done' to finish:")
bought_items = {}
while True:
    item_input = input()
    if item_input == 'done':
        break
    item, quantity = item_input.split(':')
    bought_items[item] = int(quantity)

total_bill = 0
for item, quantity in bought_items.items():
    if item in stock and stock[item] >= quantity:
        stock[item] -= quantity
        total_bill += price[item] * quantity
    else:
        print(f"Sorry, we don't have enough {item} in stock.")
print(f"\nTotal bill: ${total_bill:.2f}")
print("Remaining stock:")
for item, quantity in stock.items():
    print(f"{item}: {quantity}")
menu = {
    'pizza': 80,
    'pasta': 50,
    'burger': 70,
    'salad': 100,
    'coffee': 90,
}

# Greet the user
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs80\nPasta: Rs50\nBurger: Rs70\nSalad: Rs100\nCoffee: Rs90")

order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ").strip().lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1.title()} has been added to your order.")
else:
    print(f"Ordered item {item_1.title()} is not available yet.")

# Ask for another order
another_order = input("Do you want to order another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").strip().lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2.title()} has been added to your order.")
    else:
        print(f"Ordered item {item_2.title()} is not available!")

# Display the total amount
print(f"The total amount to pay is Rs {order_total}")

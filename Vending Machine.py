# This script simulates a vending machine transaction
# It lists all of the available options, gives displays based on different outputs, and errors when the incorrect response is inputted

# This lists all of the vending machine locations, names, prices, and associated prices
items = {
    "A1": {"name": "Doritos", "price": 2.75},
    "A2": {"name": "Cheetos", "price": 2.50},
    "A3": {"name": "Sun Chips", "price": 2.00},
    "B1": {"name": "Utz", "price": 2.25},
    "B2": {"name": "Ruffles", "price": 1.75}
}

def display_items():
    print("\nAvailable Items:")
    for code, info in items.items():
        print(f"{code}: {info['name']} - ${info['price']:.2f}")

def vending_machine():
    display_items()
    choice = input("\nEnter the item code you want: ").upper()

    # This gives an error if the inputted choice is not within the list of available options
    if choice not in items:
        print("Invalid selection. Please try again.")
        return

    # This gives an output that the following selection was made at the current market price
    item = items[choice]
    price = item["price"]
    print(f"\nYou selected {item['name']} - Price: ${price:.2f}")

    # This gives an output to insert the exact amount of money to execute the purchase of the item
    money = float(input("Insert money: $"))
    
    # This gives an error if the incorrect amount of money is inserted
    if money < price:
        print("Not enough money. Transaction cancelled.")
    else:
        change = money - price
        print(f"Dispensing {item['name']}...")  # This gives an output when the item is dispensing
        print(f"Your change is: ${change:.2f}") # Ths gives an output of the change given back
        print("Thank you for your purchase, come again soon!")   # This thanks the customer for their purchase

# This runs the vending machine

vending_machine()

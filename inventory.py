"""
Simple Inventory Management for Windows
Use loops to display or update a list of stock items
"""

# Initial inventory: list of dicts
inventory = [
    {"id": 1, "name": "Apple",  "quantity": 50,  "price": 0.50},
    {"id": 2, "name": "Banana", "quantity": 100, "price": 0.30},
    {"id": 3, "name": "Orange", "quantity": 80,  "price": 0.40},
]

def display_inventory():
    print("\nCurrent Inventory:")
    print(f"{'ID':<3} {'Name':<10} {'Qty':<5} {'Price':<6}")
    print("-" * 28)
    for item in inventory:
        print(f"{item['id']:<3} {item['name']:<10} {item['quantity']:<5} ${item['price']:<.2f}")
    print()

def add_item():
    name = input("Enter new item name: ").strip()
    try:
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
    except ValueError:
        print("Invalid number. Aborting add.")
        return
    new_id = max(item["id"] for item in inventory) + 1 if inventory else 1
    inventory.append({"id": new_id, "name": name, "quantity": qty, "price": price})
    print(f"Added {name} (ID {new_id}).")

def update_quantity():
    try:
        item_id = int(input("Enter item ID to update quantity: "))
    except ValueError:
        print("Invalid ID.")
        return
    for item in inventory:
        if item["id"] == item_id:
            try:
                new_qty = int(input(f"Enter new quantity for {item['name']}: "))
            except ValueError:
                print("Invalid quantity.")
                return
            item["quantity"] = new_qty
            print(f"Quantity of {item['name']} updated to {new_qty}.")
            return
    print("Item ID not found.")

def remove_item():
    try:
        item_id = int(input("Enter item ID to remove: "))
    except ValueError:
        print("Invalid ID.")
        return
    for i, item in enumerate(inventory):
        if item["id"] == item_id:
            removed = inventory.pop(i)
            print(f"Removed {removed['name']} (ID {item_id}).")
            return
    print("Item ID not found.")

def main_menu():
    while True:
        print("\n=== Inventory Management ===")
        print("1. Display inventory")
        print("2. Add new item")
        print("3. Update item quantity")
        print("4. Remove item")
        print("5. Exit")
        choice = input("Choose an option [1-5]: ").strip()
        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number 1-5.")

if __name__ == "__main__":
    main_menu()

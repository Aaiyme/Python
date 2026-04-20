inventory = []

while True:
    print("1. Add | 2. View | 3. Update | 4. Delete")
    choice = input("Select Option: ")

    if choice == "1":
        name = input("Enter product: ")
        item = {"name": name}
        inventory.append(item)
        print(f'"{name}" added to inventory.')

    elif choice == "2":
        if not inventory:
            print("Inventory is empty.")
        else: 
            print("Current inventory:")
            for item in inventory:
                print("-", item["name"])

    elif choice == "3":
        target = input("Enter item name to update: ")
        found = False
        for item in inventory:
            if item["name"].lower() == target.lower():
                new_name = input("Enter new product name: ")
                item["name"] = new_name
                print(f'{target}" update to "{new_name}".')
                found = True
                break

        if not found:
            print("Item not in Inventory!")  

    elif choice == "4":
        target = input("Enter item to remove: ")
        found = False
        for item in inventory:
            if item["name"].lower() == target.lower():
                inventory.remove(item)
                print(f"{target} succesfully removed")
                found = True
                break
        if not found:
                print("Item is not in Inventory")

    elif choice == "5":
        print("The system is closed")

    else: 
        print("Invalid option. Please try again.")

    choice = input("Do you want to continue? (Y/N): ")
    if choice.lower() == "n":
            break
items = []
quantities = []

def inventory(names, counts):
    if not names:
        return "Empty Backpack"

    length = min(len(names), len(counts))
    return "".join(f"{i + 1}. {names[i]} x{counts[i]}\n" for i in range(length))

while True:
    try:
        item = input("Add item: (or type 'exit' to quit): ")

        if item.lower() == "exit":
            print("FInal inventory:")
            print(inventory(items, quantities))
            break
        
        if item in items:
            print("You already have that item")
            continue

        qty = int(input(f"How many {item}? "))
        
        items.append(item)
        quantities.append(qty)

    except ValueError:
        print("Use numbers only")

    

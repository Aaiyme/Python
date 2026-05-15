items = []

while True:
    get_item1 = input("Enter item: ").strip()
    if not get_item1:
        print("Cannot be blank!")
        continue

    items.append(get_item1)
    break

while True:
    get_item2 = input("Enter item: ").strip()
    if not get_item2:
        print("Cannot be blank!")
        continue

    items.append(get_item2)
    break

while True:
    get_item3 = input("Enter item: ").strip()
    if not get_item3:
        print("Cannot be blank!")
        continue

    items.append(get_item3)

    choice = input("Do you want to continue? (Y/N): ").strip().lower()
    if not choice:
        print("Cannot be blank!")
    if choice == "y":
        continue
    else:
        print("Final List:")
        for item in items:
            print(item)
    break
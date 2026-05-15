items = []

for i in range(1, 4):
    while True:
        item = input(f"Enter item {i}: ").strip()
        if not item:
            print("Cannot be blank!")
            continue

        items.append(item)
        break

    choice = input("Do you want to continue? (Y/N): ").strip().lower()
    if not choice:
        print("Cannot be blank!")
        continue

    if choice == "y":
        continue
    else:
        print("Final List:")
        for item in items:
            print(item)
        break

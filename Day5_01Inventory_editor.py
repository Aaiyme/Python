
inventory = [
        {"name": "coke", "price": 20, "stocks": 10},
        {"name":"bread", "price": 5, "stocks": 10}
]
while True:
    search_name = input("Enter product to update: (or type 'exit') ").strip()

    if search_name.lower() == "exit":
        break

    found = False
    for item in inventory:
        if item["name"].lower() == search_name.lower():  
            try:
                input_stocks = int(input("Enter stocks: ").strip())
                item["stocks"] = input_stocks
                found = True
            except ValueError:
                print("Invalid Input")
                found = True
                break

    if not found:
        print("The product not found!")
    for i in inventory:
        print(f"{i['name'].capitalize()}: ₱{i['price']}, {i['stocks']} in stocks")
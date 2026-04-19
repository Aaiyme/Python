all_items = []

while True:                                                                                                                                                                                                                                                                            
    product = {}

    while True:
            name = input("Enter the product name: ")
            if name.strip():
                product["name"] = name
                break
            print("Cannot be blank")

    while True:
        try:
            p = float(input(f"Price of the {product['name']}: ").strip())
            product["price"] = p
            break
        except ValueError:
            print("Price only!")

    while True:
        try:
            s = int(input(f"stocks of the {product['name']} ").strip())
            product["stocks"] = s
            product["status"] = "Out of Stocks" if s <= 0 else "In Stocks"
            break
        except ValueError:
            print("Error: Enter a valid number for stock!")

    all_items.append(product)
    print(f"{product['name']} Added!")

    choice = input("Do you want to continue? (Y/N)")
    if choice.lower() == "n":
                break
print("=====Inventory======")
grand_total = 0
for item in all_items:
    item_value = item["price"] * item["stocks"]
    grand_total += item_value
    print(f"Product name: {item['name']}, Price: {item['price']}, Stocks: {item['stocks']}, Status: {item['status']}")

    print(f"\n Total Inventory Value = {grand_total}")





        






    
    
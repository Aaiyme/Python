def calculate_bill(hours):
    total = hours * 20
    if value >= 5: 
            total = total - 30
    return total

while True:
    try:
        input_customer_ID = input("Enter ID name: ")
        if not input_customer_ID.strip():
            print ("This cannot to be a blank!")
            continue

        raw = input("How many hours?: ")
        if not raw.strip():
            print("This cannot to be a blank!")
            continue

        value = int(raw)

        result = calculate_bill(value)
        print(f"Customer: {input_customer_ID}, total bill is: {result}")
       

        choice = input("You want to continue? (Y/N): ")
        if choice.lower() == "n":
            print("Goodbye! the system is turn off")

    except ValueError:
        print("Invalid! Please number of hours only")
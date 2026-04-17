def check_entry(age): 
    return "Welcome to the club" if age >= 18 else "Go home, kid!"
    
while True:
    try:
        input_name = input("Enter ur name: ")
        if not input_name.strip():
            print("cannot to be blank")
            continue

        input_age = int(input("Enter ur age: "))
        result = check_entry(input_age)
        print(f"Hi {input_name}, {result}")
    except ValueError:
        print("Invalid input! Please enter a number only")
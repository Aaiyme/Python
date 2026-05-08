def age_checker(age):
    if age >= 75:
        return "Elderly"
    elif age >= 60:
        return "Senior-Adult"
    elif age >= 26:
        return "Middle-Age"
    elif age >= 18:
        return "Young-Adult"
    elif age >= 13:
        return "Minor"
    else:
        return "Child"
    
while True:
    get_name = input("Enter your name: ").strip()
    if not get_name:
        print("cannot be blank")
        continue

    while True:
        age_input = input(f"Enter age for {get_name}: ").strip()
        if not age_input:
            print("Age cannot be blank!")
            continue 
        try:
            age = int(age_input)
            break

        except ValueError:
            print("Invalid! Please enter a number for your age.")
            continue    

    category = age_checker(age)
    print(f"Hi {get_name}! you are {age_input} and a {category}")

    choice = input("Do you want to continue? (Y/N): ")
    if choice.lower() == "n":
        print("goodbye")
        break
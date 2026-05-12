def age_check(age):
    if age >= 60:
        return "Senior"
    elif age >= 20:
        return "Adult"
    elif age >= 13:
        return "Teen"
    else:
        return "Child"
while True: 
    while True:
        get_fname = input("Enter first name: ").strip()
        if not get_fname:
            print("First name cannot be blank!")
            continue
        get_lname = input("Enter last name: ").strip()
        if not get_lname:
            print("Last name cannot be blank!")
            continue
        break

    while True:
        try:
            get_age = input("Enter age: ").strip()
            if not get_age:
                print("Age cannot be blank!")
                continue

            age = int(get_age)
            category = age_check(age)

        except ValueError:
            print("Error! Age only")
            continue
        break

    while True:
        get_languages = input("Enter favorite programming languages: ").strip()
        if not get_languages:
            print("Favorite programming languages cannot be blank")
            continue
        break

    print("")
    print("Generating Profile...")

    for i in range(1,4):
        print(i)

    print("===== PROFILE SUMMARY =====")
    print(f"name: {get_fname} {get_lname}")
    print(f"Age: {age}")
    print(f"Category: {category}")
    print(f"Favorite programming language: {get_languages}")
    print("")

    choice = input("Do you want to create another profile? (Y/N): ").strip().lower()

    if choice == "y":
        continue
    else:
        print("System is closed!")
        break


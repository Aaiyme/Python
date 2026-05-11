def age_category(age):
    if age >= 20:
        return "Adult"
    elif age >= 13:
        return "Teen"
    else:
        return "Child"
    
while True:
    get_name = input("Enter student name: ").strip()
    if not get_name:
        print("Cannot be blank!")
        continue
    break

while True:
    try:
        get_age = input("Enter student age: ").strip()
        if not get_age:
            print("Cannot be blank!")
            continue
        value = int(get_age)
       
    except ValueError:
        print("Error! Age only")
        continue
    break

category = age_category(value)
    
print(f"Welcome {get_name}!")
print(f"You are {value} years old.")
print(f"Category: {category}")
print(f"Generating Report....")
for i in range(1, 6):
    print(i)



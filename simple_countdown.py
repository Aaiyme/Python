while True:
    num = 10
    while num >= 1:
        print(num)
        num -= 1 
    print("Blast!")
    
    choice = input("Do you want to continue? (Y/N): ").strip().lower()
    if choice == "y":
        continue
    else:
        print("System is closed!")
        break

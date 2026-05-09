stored_username = "hayme"
stored_admin_username = "admin"
stored_password = "asd1"

while True:
    attempts = 0
    max_tries = 3
    authenticated = False

    while attempts < max_tries:
        username = input(f"Enter username: {attempts + 1}/{max_tries}: ").strip()

        if not username:
            print("Cannot be blank!")
            continue

        if username == stored_username or username == stored_admin_username:
            if username == stored_admin_username:
                print("Welcome to admin panel")
            authenticated = True
            break
        else: 
            attempts += 1
            print(f"Wrong Username. {max_tries - attempts} attempts left")
            
    if not authenticated:
        print("System is locked.")
        break

    attempts = 0
    while attempts < max_tries:
        password = input(f"Enter password {attempts + 1}/{max_tries}: ").strip()

        if not password:
            print("Cannot be blank!")
            continue

        if password == stored_password:
            print("Access Granted!")
            break
        else:
            attempts += 1
            print(f"Wrong password({max_tries - attempts}) attemps left.")
    else:
        print("Incorrect password. Returning to start...")
        continue

    choice = input("Do you want to continue? (Y/N): ").strip().lower()
    if choice == "y":
        print("System restarting")
        continue
    else:
        print("Goodbye")
        break
        
    
    


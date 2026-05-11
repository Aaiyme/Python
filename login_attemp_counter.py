stored_username = "hayme"
stored_password = "password"
stored_admin_username = "noctis"

while True:
    max_tries = 3
    attempts = 0
    authentication = False

    while attempts < max_tries:  
        username = input("Enter username: ").strip()
        if not username:
            print("Cannot be blank!")
            continue

        password = input("Enter password: ").strip()
        if not password:
            print("Cannot be blank!")
            continue

        if (
            username == stored_username and password == stored_password
        ) or (
            username == stored_admin_username and password == stored_password
        ):
            print("Access Granted!!")

            if username == stored_admin_username:
                print("Welcome to admin panel")
                print("Loading...")
                for i in range(1, 4):
                    print(i)

            authentication = True
            break       

        else:
            attempts += 1
            print("Wrong username or password.")
            print(f"Attempts: {max_tries - attempts}")
            
    if authentication:
        break
    
    print("No attempts left.")
    break
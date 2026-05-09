stored_username = "hayme"
stored_password = "lazy"


while True:
    username = input("Enter Username: ").strip()
    if not username:
        print("Cannot be blank!")
        continue
    if username == stored_username:
        break

while True:
    password = input("Enter password: ").strip()
    if not password:
        print("Cannot be blank")
        continue
    if password == stored_password:
        print("Success")
        break
    else:
        print("Wrong password")

choice = input("Do you want to continue? (Y/N): ").strip().lower()
if choice == "y":
    print("Restart program (rerun manually / wrap in outer loop if needed)")
else:
    print("Goodbye")



    





    




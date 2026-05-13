balance = 1000


while True:
    try:
        get_menu = input("1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit | : " ).strip()
        if not get_menu:
            print("Cannot be blank!")
            continue

        menu = int(get_menu)

        if menu == 1:
            print(f"Your balance is: {balance}")

        elif menu == 2:
            get_deposit = input("How much deposit: ").strip()
            if not get_deposit:
                print("Cannot be blank!")
                continue

            deposit = int(get_deposit)
            balance += deposit
            print(f"Successfully deposit! Your current balance is: {balance}")


        elif menu == 3:
            get_withdraw = input("How much you withdraw?: ").strip()
            if not get_withdraw:
                print("Cannot be blank!")
                continue

            withdraw = int(get_withdraw)

            if balance < withdraw:
                print("Inefficient Balance")
            else:
                balance -= withdraw
                print(f"Withdraw is Successfull. Your current balance is: {balance}")

        elif menu == 4:
                print("The system is closed!")
                break
        else:
            print("Invalid! select number on the menu only!")

    except ValueError:
        print("Numbers only")
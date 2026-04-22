import os

all_loans = []
if os.path.exists("loan_database.txt"):
    try:
        with open("loan_database.txt", "r") as file:
            for line in file:
                # Format: mode,amount,payment,total_paid
                data = line.strip().split(",")
                if len(data) == 4:
                    all_loans.append({
                        "mode": data[0],
                        "amount": float(data[1]),
                        "payment": float(data[2]),
                        "total_paid": float(data[3])
                    })
        print(f"Successfully loaded {len(all_loans)} existing loans.")
    except Exception:
        print("Could not read database. Starting fresh.")

all_loans = []

while True:
    try:
        raw_income = input("Enter your daily income: ").strip()
        if not raw_income:
            print("Error: Income cannot be blank!")
            continue
        daily_income = float(raw_income)
        break 
    except ValueError:
        print("Error: Please enter a valid number (e.g. 500.00)")

while True:
    loan = {}

    while True:
        mode_input = input("\nIs this a Daily or Weekly loan? (D/W): ").strip().lower()
        if mode_input in ["d", "w", "daily", "weekly"]:
            # Standardize it to just 'd' or 'w'
            loan["mode"] = mode_input[0] 
            break
        print("Error: Please type 'D' for Daily or 'W' for Weekly.")

    while True:
        try:
            loan["amount"] = float(input("How much was the original loan?: "))
            loan["payment"] = float(input(f"How much is the {loan['mode']} payment?: "))
            loan["total_paid"] = float(input("How much is the FULL amount to be paid?: "))

            if loan["total_paid"] < loan["amount"]:
                print("Warning: Total paid is less than the loan. Is that correct?")
            break
        except ValueError:
            print("Error: Numbers only for money fields!")

    all_loans.append(loan)

    another = input("\nDo you have another loan? (Y/N): ").strip().lower()
    if another == "n":
        break

total_daily_loans = 0
total_weekly_daily_equiv = 0

for item in all_loans:
    if item["mode"] == "d":
        total_daily_loans += item["payment"]
    else: 
        total_weekly_daily_equiv += (item["payment"] / 7)

total_daily_burden = total_daily_loans + total_weekly_daily_equiv
surplus = daily_income - total_daily_burden

print("\n" + "="*30)
print("       FINANCIAL REPORT")
print("="*30)
print(f"Daily Income:      ₱{daily_income:,.2f}")
print(f"Daily Loan Fees:   ₱{total_daily_loans:,.2f}")
print(f"Weekly (per day):  ₱{total_weekly_daily_equiv:,.2f}")
print("-" * 30)
print(f"TOTAL DAILY DEBT:  ₱{total_daily_burden:,.2f}")
print(f"NET SURPLUS:       ₱{surplus:,.2f}")

if surplus > 500:
    print("\n STATUS: Safe. You can afford your needs.")
elif 0 <= surplus <= 500:
    print("\n STATUS: Risky! Petsa de Peligro vibes.")
else:
    print("\n STATUS: CRASHOUT! Debt is higher than income.")
print("="*30)

with open("loan_database.txt", "w") as file:
    for loan in all_loans:
        line = f"{loan['mode']},{loan['amount']},{loan['payment']},{loan['total_paid']}\n"
        file.write(line)

print("\n💾 Database updated! All loans are saved.")
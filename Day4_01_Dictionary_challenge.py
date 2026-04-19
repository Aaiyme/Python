champ_stats = {}

while True:
    champion = input("Enter Champion: ")
    if champion.strip():
        champ_stats["champion"] = champion
        break
    print("Cannot be blank")

while True:
    champion_role = input("Enter Role: ")
    if champion_role.strip():
        champ_stats["champion_role"] = champion_role
        break
    print("Cannot be blank")

while True:
    try:
        champion_wr = float(input("Enter Winrate: "))
        champ_stats["champion_wr"] = champion_wr

        if champion_wr >= 90:
            champ_stats["rank"] = "Pro level"
        elif champion_wr >= 50:
            champ_stats["rank"] = "Intermidiate Level"
        else:
            champ_stats["rank"] = "Noob! Play more efficiently"
            print(f"Status assign: {champ_stats['rank']}")
        break

    except ValueError:
        print("Please enter a decimal number!")

print("\n==== Champion Profile ====")
print(f"Champion {champ_stats['champion']}")
print(f"Champion Role {champ_stats['champion_role']}")
print(f"Champion Winrate {champ_stats['champion_wr']}% - {champ_stats['rank']}")

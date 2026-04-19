def is_valid(text):
    return bool(text.strip())

my_pool = []

while True:
        champion_1 = input("Enter First Champion: ")
        if champion_1.strip():
            my_pool.append(champion_1)
            break
        print("cannot be blank")
while True:
        champion_2 = input("Enter Second Champion: ")
        if champion_2.strip():
            my_pool.append(champion_2)
            break
        print("cannot be blank")
while True:
        champion_3 = input("Enter Third Champion: ")
        if champion_3.strip():
            my_pool.append(champion_3)
            break
        print("cannot be blank")

print(f"My top 3 champions is: {my_pool}")

inventory = []

try:
    with open ("inventory.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
        
            item = {
                "n": data[0],
                "p": float(data[1]),
                "s": int(data[2])
            }
            inventory.append(item)
    print("Previous data loaded successfully!")
except FileNotFoundError:
    print ("No save data")

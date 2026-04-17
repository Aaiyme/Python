def calculate_gold(minions,  kills,  assist):
    return 500 + (minions * 20) + (kills * 300) + (assist * 150)
    
while True:
    try:
        input_minions_kills = int(input("How many minions did you kill?: "))

        input_kills = int(input("How many kills you have?: "))

        input_assists = int(input("How many assist you have?:"))

        result = calculate_gold(input_minions_kills, input_kills, input_assists)
        if result >= 3200:
            print ("You can buy Legendary Item")
        else:
            needed = 3200 - result
            print("Keep farming! You need")
    
        
        choice = input("You want to try more? (Y/N)")
        if choice.lower() == "n":
                print("Goodbye! system is out")
                break    
    except ValueError:
        print("Please numbers only")



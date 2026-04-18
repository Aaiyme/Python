inventory = []
    

def show_inventory(item_list):
        if len(item_list) == 0:
            return"inventory is empty."
        return f"Inventory: {', '.join(item_list)}"

def exit_message():
      return "The system is Closed."

while True:
        try:
                input_item = input("Add item (or type 'view' or type 'exit' to close the system.): ")

                if input_item.lower() == "view":
                        result = show_inventory(inventory)
                        print(result)


                elif input_item.lower() == "exit":
                     result = exit_message()
                     print(result)
                     break

                elif not input_item.strip():
                    print("This is not to be a blank!")
                    continue
                else:
                        inventory.append(input_item)
                        print("Succesfully added!")


        except ValueError:
            print("Invalid Value")
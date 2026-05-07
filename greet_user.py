def get_user_name():
    return input("Enter your name: ").strip()

def get_user_age():
    return int(input("Enter your age: ")) 
 

def greet(name, age):
    return f"Hello {name}! You are {age}. It's a pleasure to meet you"

name = get_user_name()
age = get_user_age()

result = greet(name, age)
print(result)
    


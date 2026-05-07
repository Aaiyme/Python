def get_name():
    return input("Enter name: ")

def get_age():
    return int(input("Enter age: "))


def get_height():
    return float(input("What is your Height?: "))


def message(name, age, height):
    return f"Hello! {name} you are {age} and you are {height} tall"

name = get_name()
age = get_age()
height = get_height()
namedata = type(name).__name__
agedata = type(age).__name__
heightdata = type(height).__name__



result = message(name, age, height)
print(result)
print(f"Name type: {namedata}")
print(f"Age type: {agedata}")
print(f"Height type: {heightdata}")





def check_grade(grade):
    if grade < 0 or grade > 100:
        return "Invalid grade"
    elif grade >= 90:
        return "Exellent! A+"
    elif grade >= 75:
        return "Passed! Good job"
    else:
        return "Failed! bobo ka"

while True:
    try:
        input_student_name = input("Enter student name: ")
        if not input_student_name.strip():
            print("Cannot to be a blank!")
            continue


        input_student_grade = int(input("Enter student grade: "))
        result = check_grade(input_student_grade)
        print(f"{input_student_name}, {result}")

        choice = input("Do you want to continue?: (N/Y) ")
        if choice.lower() == "n":
            print("Goobye!")   
            break

    except ValueError:
        print("Invalid! grades only")


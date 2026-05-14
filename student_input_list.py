students = []

while True:
    get_student_1 = input("Enter student 1: ").strip()
    if not get_student_1:
        print("Cannot be blank")
        continue

    students.append(get_student_1)
    break

while True:
    get_student_2 = input("Enter student 2: ").strip()
    if not get_student_2:
        print("Cannot be blank!")
        continue

    students.append(get_student_2)
    break

while True:
    get_student_3 = input("Enter student 3: ").strip()
    if not get_student_3:
        print("Cannot be blank!")
        continue

    students.append(get_student_3)
    break

while True:
    get_student_4 = input("Enter student 4: ").strip()
    if not get_student_4:
        print("Cannot be blank!")
        continue

    students.append(get_student_4)
    break

while True:
    get_student_5 = input("Enter student 5: ").strip()
    if not get_student_5:
        print("Cannot be blank!")
        continue

    students.append(get_student_5)
    break


for student in students:
    print(student)

count = 0

for student in students:
    count += 1
print(f"\nNumber of students: {count}")





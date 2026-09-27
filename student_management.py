students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student Name: ")
        marks = float(input("Marks: "))
        students[name] = marks
        print("Student Added!")

    elif choice == "2":
        for name, marks in students.items():
            print(f"{name}: {marks}")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            print(f"Marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == "4":
        break

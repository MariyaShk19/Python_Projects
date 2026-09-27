employees = {}

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        salary = float(input("Salary: "))
        employees[name] = salary

    elif choice == "2":
        for name, salary in employees.items():
            print(name, "-", salary)

    elif choice == "3":
        break

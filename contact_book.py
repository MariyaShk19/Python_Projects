contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        contacts[name] = number

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        name = input("Search Name: ")
        print(contacts.get(name, "Not Found"))

    elif choice == "4":
        break

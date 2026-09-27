books = ["Python", "Java", "C++"]

while True:
    print("\n1. View Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available Books:")
        for book in books:
            print(book)

    elif choice == "2":
        book = input("Enter book name: ")
        if book in books:
            books.remove(book)
            print("Book Issued")
        else:
            print("Book Not Available")

    elif choice == "3":
        book = input("Enter returned book: ")
        books.append(book)
        print("Book Returned")

    elif choice == "4":
        break

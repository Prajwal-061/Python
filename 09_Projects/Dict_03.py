library = {}
def addBook(library):
    BookId=input("Enter the book Id")
    title=input("Enter the title of book:")
    author=input("Enter the author of the book:")
    if BookId in library:
        print("Book is already in the library")
    else:
        library[BookId]={"title":title,
                         "author":author,
                         "available": True}

    print("Book added to Library")


def displayBook(library):
    for name,book in library.items():
        print(f"Book Id:{name}")
        print(f"Title:{book['title']}\nAuthor:{book['author']}\nAvailability:{ 'Yes'  if book['available'] else 'NO'}\n")


def borrowBook(library):
    BookId=input("Enter the of the book you want to borrow:")
    if BookId in library and library[BookId]['available']==True:
        print(f" Book {BookId} is borrowd successfully")
        library[BookId]['available']=False
    else:
        print(" Book not available or invalid Id")


def returnBook(library):
    BookId=input("Enter the book id:")
    if BookId in library and library[BookId]['available']==False:
        print("Book Returned successfully")
        library[BookId]['available'] = True
    else:
        print("Book already exists or invalid Id")


def searchBook(library):
    BookId=input("Enter the bookID:")
    if BookId in library:
        print("Book Found")
        book=library[BookId]
        print(f"Book Id:{BookId}")
        print(f"Title:{book['title']}\n Author:{book['author']}\n  {'Yes' if book['available'] else 'No'}\n")
    else:
        print("Book not found or invalid BookID")



while True:
    print("\n--- Library Management Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addBook(library)
    elif choice == "2":
        displayBook(library)
    elif choice == "3":
        borrowBook(library)
    elif choice == "4":
        returnBook(library)
    elif choice == "5":
        searchBook(library)
    elif choice == "6":
        print("Exiting the Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")




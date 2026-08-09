def print_books():
    for book_id in books:
        if(books[book_id]["issued"]==True):
            print(f"{book_id}\t{books[book_id]["name"]}\tIssued")
        else:
            print(f"{book_id}\t{books[book_id]["name"]}\tAvailable ")
def issue_book():
    book_id = int(input("Enter book id: "))
    if book_id in books:
        if books[book_id]["issued"]==False :
            books[book_id]["issued"]=True
            print("Book issued successfully")
        else:
            print("Book already issued")
    else:
        print("Book not found")
def return_book():
    book_id = int(input("Enter book id to return the book : "))
    if book_id in books:
        if books[book_id]["issued"]==False :
            print("Book is already available.")
        else:
            books[book_id]["issued"]=False
            print("Book returned successfully!")
    else:
        print("Book not found")
def search_book():
    book_id = int(input("Enter book id to search: "))
    if book_id in books:
        if books[book_id]["issued"]==False :
            print(f"{book_id}\t{books[book_id]["name"]}\tAvailable")
        else:
            print(f"{book_id}\t{books[book_id]["name"]}\tIssued")
    else:
        print("Book not found")
books = {
    101:{
        "name":"The Great Gatsby", 
        "issued":True
    },
    102:{
        "name":"To Kill a Mockingbird", 
        "issued":True
    },
    103:{
        "name": "1984",
        "issued":False
    }, 
    104:{
        "name": "Pride and Prejudice",
        "issued":False
    }, 
    105:{
        "name": "The Catcher in the Rye",
        "issued":True
    }}

print_books()
while True:
    print("-------------MENU-------------")
    print("1. Enter 1 for issuing a book")
    print("2. Enter 2 for returning a book")
    print("3. Enter 3 for searching a book")
    print("4. Enter 4 to Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
       issue_book()
       print_books()
    elif choice == "2":
        return_book()
        print_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
   
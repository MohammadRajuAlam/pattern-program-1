# wap to display the name of the day, take the number as input from user
def day_name(day):
    if day==1: 
        print("Monday- working day")
    elif day==2:
        print("Tuesday- working day")
    elif day==3:
        print("Wednesday")
    elif day==4:
        print("Thursday- working day")
    elif day==5:
        print("Friday- working day")
    elif day==6:
        print("Saturday- holiday")
    elif day==7:
        print("Sunday- Holiday")
    else:
        print("Invalid day number")
day=int(input("Enter the day number: "))
day_name(day)

# wap to check the requred book is available in the library or not, take the name of the book as input from user
def check_book(book_name):
    library_books=["python", "data science", "machine learning", "artificial intelligence", "deep learning"]
    if book_name in library_books:
        print(f"{book_name} is available in the library")
    else:
        print(f"{book_name} is not available in the library")

book=input("Enter the name of the book: ")
check_book(book)
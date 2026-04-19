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
        print("Invalid day number, number should be between 1 to 7")
day=int(input("Enter the day number: "))
day_name(day)

# Wap to display the name of the month, take the number as input from user
def month_name(month):
    if month==1:
        print("January")
    elif month==2:
        print("February")
    elif month==3:
        print("March")
    elif month==4:
        print("April")
    elif month==5:
        print("May")
    elif month==6:
        print("June")
    elif month==7:
        print("July")
    elif month==8:
        print("August")
    elif month==9:
        print("September")
    elif month==10:
        print("October")
    elif month==11:
        print("November")
    elif month==12:
        print("December")
    else:
        print("Invalid month number, number should be between 1 to 12")

month=int(input("Enter the month number: "))
month_name(month)
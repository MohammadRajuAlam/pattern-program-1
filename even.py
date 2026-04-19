# wap to display whether the number is even or odd, take the number as input from user
def even():
    num=int(input("Enter the number"))
    if num%2==0:
        print(f"num is even: {num}")
    else:
        print(f"Number is odd: {num} ")
        
even()
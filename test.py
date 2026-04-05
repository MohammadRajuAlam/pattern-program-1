# find even num from 2 to 50, User can take any input

def even(num):
    for i in num: 
        if i %2==0 and i<=52:
            print(f"even num {i}")
        else:
            break
a=int(input("Enter the num"))
even(a)
        
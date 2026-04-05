# find odd num from 1 to 101, Here user can take any number
def odd(num):
    for i in num:
        if i%2 !=2 and i<=101:
            print(f"Even num {i}")
        else:
            break
a=int(input("Enter the number"))
odd(a)
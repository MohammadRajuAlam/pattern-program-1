# check given number is even or odd
def even_odd(num):
    if num %2==2:
        print(f"even no {num}")
    else:
        print(f"odd no {num} ")
a=int(input("Enter the num"))
even_odd(a)
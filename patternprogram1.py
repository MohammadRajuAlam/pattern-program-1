# p 1) wap to display 
             * * * * *
             * * * * *
             * * * * *
             * * * * *  

# 1 solution using for loop
 
num=int(input("Enter rows:"))

for i in range(1,num+1):
    print("* "*num, end="")
    print()

# 2 salution

def pt(a,b):
            
    for i in range(1,rows+1):
        for j in range(1,colm+1):
            print("*", end=" ")
        print()

rows=int(input("Enter no of rows:"))
colm=int(input("Enter no of colmns:"))

pt(rows,colm)

# 3 using while loop with fun

def pt(a):
    s=1
    while a>=s:
       print("* "*a)
       s=s+1
    print()
num=int(input("Ente no of rows: "))
pt(num)

# Wap to dispay your infomation, take input from user in user define function 

def info(name, age,address,phone,email,qual,gender): 
    print(f"Name: {name}\nAge: {age}\naddress: {address}\nPhone No: {phone}\nEmail: {email}\nQualification: {qual}\nGender: {gender}")
    
Name=input("Enter your name:")
Age=int(input("Enter Your age:"))
Add=input("Enter your address:")
Phone=int(input("Enter your phone No:"))
Email=input("Enter your Email Id:")
Q=input("Enter you Qualification:")
Sex=input("Enter your Gender:")

info(Name, Age,Add,Phone,Email,Q,Sex)

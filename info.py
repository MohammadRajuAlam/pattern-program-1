# Wap to dispay your infomation, take input from user in user define function 

def info(name, age,address,phone,email,qual,gender,marrage_status): 
    print(f"Name: {name}\nAge: {age}\naddress: {address}\nPhone No: {phone}\nEmail: {email}\nQualification: {qual}\nGender: {gender}\nMarrage Status: {marrage_status}")
    
Name=input("Enter your name:")
Age=int(input("Enter Your age:"))
Add=input("Enter your address:")
Phone=int(input("Enter your phone No:"))
Email=input("Enter your Email Id:")
Q=input("Enter you Qualification:")
Sex=input("Enter your Gender:")
M=input("Enter your Marrage Status:")

info(Name, Age,Add,Phone,Email,Q,Sex,M)

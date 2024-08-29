from datetime import datetime
class Bank_System:
    bank_name="ICICI Bank" # Here All class/static variable written inside class but outside class's method
    location="Bangalore"
    __bank_id=576321
    
    def __init__(self,holder,acc,psswd,acc_type,balance): # This is constructor method
        self.holder_name=holder     
        self.account_no=acc
        self.__password=psswd
        self.account_type=acc_type
        self.balance=balance
        
    def get_acc_detail(self): # Instance Method for accessing instance variable
        print(f"Holder Name: {self.holder_name}\nAccount No: {self.account_no}\nAccount Type: {self.account_type}\nCurrent Balance: {self.get_balance()}")
        
    def get_holder_details(self): # This instance method with local variable
        father_name="Abdul"  # These are local variables
        mother_name="Abada"
        dob='20/02/1998'
        address='Electronic City Bangalore'
        city="Bangalore"
        pin_code=560072
        state="Karnataka"
        country="India"
        print(f"Father's Name: {father_name}\nMother's Name: {mother_name}\nDOB: {dob}\nAddress: {address}\nCity: {city}\nPin Code: {pin_code}\nState:{state}\nCountry: {country}")
    
    def credit(self,amount): # This is instance Method
        if amount>0:
            self.balance+=amount
            print(f"Rs {amount} was Credited\nCurrent Balance: {self.get_balance()}")
        else:
            print(f"{amount} invalid amount")
        
    def debit(self,amount): 
        if amount>0:
            self.balance-=amount
            print(f"Rs {amount} was debited\nCurrent Balance: {self.get_balance()}")
        else:
            print(f"{amount} invalid amount\nplease Enter valid amount")
            
    def get_balance(self):
        return self.balance
    
    @classmethod
    def get_bank_details(cls): # This is class Method for access class/static variables
        print(f"Bank Name: {cls.bank_name}\nLocation: {cls.location}\nBank Id: {cls.__bank_id}")
        
    @staticmethod
    class nomenee_detail():  # This is static method
        pass # Here we can write more code
      
bank=Bank_System("Md Arif",123456789,"ertf786j","Salary",5000)
#bank.get_acc_detail() # Here we can access Acc details
#bank.get_holder_details() # Here We can access Acc holder details
#Bank_System.get_bank_details() # Here We can access class variable in bank details usig class Name or object name with class method    
#bank.get_bank_details() # Here We can also access class variable using object name with class method
#bank.credit(amount=int(input("Enter credit amount\n"))) # Here we can Enter Credit amount
#bank.debit(amount=int(input("Enter debit amount\n")))  # Here We can Enter Debit amount
bank.get_acc_detail() # Here we can access Acc details with balance after Credite/Debited
#print(bank.get_balance()) # Here We can access balance using method
#del bank # Here We can delete created object
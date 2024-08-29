# Create User Exception
# Wap to withdraw money from ICICI bank in bank having some conditions
# 1) Balance in bank should not be less than 1000
# 2) User Account will be Block for an hour if user entered 3 times worong pin

import time  # Here time is a built-in module

class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

pin_attempt = 1  # Here storing the attempts

def withdraw():
    global pin_attempt

    pin_saved = 12340  # Suppose password already saved in db
    Acc_Balance = 10000  

    if pin_attempt > 3:
        print("Too many incorrect attempts. Your account is blocked for an hour.")
        time.sleep(3600)
        

    pin = int(input("Enter the PIN:\n"))

    if pin == pin_saved:
        try:
            amount = float(input("Enter Amount to withdraw:\n"))
            current_balance = Acc_Balance - amount

            if current_balance < 1000:
                raise BalanceExceptionError("Insufficient balance in your account.")

            print(f"Withdrawal successful!\nCurrent Balance: {current_balance}")

        except BalanceExceptionError as bal:
            print(bal)
            #print(bal.__class__)

    else:
        pin_attempt += 1
        print("Wrong PIN.")
        ans = input("Do you want to continue? (y/n): ")

        if ans.lower() == 'y':
            withdraw()
        else:
            print("Thank you for using ICICI Bank.")
        

withdraw()

    

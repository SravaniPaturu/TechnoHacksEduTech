#Program for ATM Stimulator

print("Please insert your card")

user_name=input("Enter the User_name:")

password=int(input("Enter your password:"))

pin=int(input("Enter your atm pin:"))

balance=5000

if pin==password:
    
    while True:
       
        #ATM Functionalities and operations
        print("1.Balance\n","2.Deposit\n","3.With_draw\n","4.Exit")

        choice=int(input("Enter your choice:"))
        
        #To check the balance in account
        if choice==1:
            print("Your current balance is:",balance)
        
        #To deposit amount into account
        elif choice==2:
            deposit_amount=int(input("Please enter amount to be deposited:"))

            balance=balance+deposit_amount

            print(user_name,deposit_amount,"has been deposited into your account")

            print("your updated balance is",balance)
        
        #To withdraw amount from account
        elif choice==3:
            withdraw_amount=int(input("Enter the amount to withdraw:"))

            if withdraw_amount>balance:
                print("Insufficient balance")

            else:
                balance=balance-withdraw_amount

                print(user_name,withdraw_amount,"has been debited from your account")

                print("your updated balance is",balance)
    
        elif choice==4:
            break

else:
    print("pin is wrongly entered")
    


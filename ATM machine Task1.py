import time
print("please insert your ATM card")
time.sleep(5)
password=1234
transaction_history=[]
pin=int(input("enter your ATM pin: "))
balance = 10000
if pin == password:
    while True:
        
        print("""
              1 == balance
              2 == cash withdrawal
              3 == cash deposit
              4 == pin change
              5 == transcation history
              6 == exit
              """)
        try:
            option = int(input("enter your choice: "))
        except:
            print("please enter valid option")
            continue    

        #1.checking balace
            
        if option == 1:
            print(f"your current balance is {balance}")

        #2.Cash withdrawal(Amount is debited from your account)

        elif option == 2:
            withdraw_amount = int(input("please enter withdraw_amount: "))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your current balance is {balance}")
            transaction_history.append(f"debited:{withdraw_amount}")
            print(f"{transaction_history}")

        #3.Cash deposited(Amount is credited to your account)

        elif option == 3:
            deposit_amount = int(input("please enter deposit_amount: "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your current balance is {balance}")
            transaction_history.append(f"credited:{deposit_amount}")
            print(f"{transaction_history}")

        #4. changing ATM pin

        elif option == 4:
            old_pin = int(input("enter your current pin: "))
            if old_pin == pin:
                new_pin = input("enter your new pin: ")
                confirm_pin = input("confirm your pin: ")
                if new_pin == confirm_pin:
                    pin == new_pin
                    print("your pin has been changed successfully")
                    transaction_history.append("pin change")
                    print(f"{transaction_history}")
                else:
                    print("pin doesn't match")
            else:
                print("incorrect pin, please try again")

        #5. Transaction History

        elif option == 5:
            print(f"your transaction History is {transaction_history}")
            print(f"{transaction_history}")

        #6. Exit

        elif option == 6:
            print("Thank you for using ATM. Goodbye!")
            break

       
    else:
        print("invalid option")

else:
    print("wrong pin please try again")

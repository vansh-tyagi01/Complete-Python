name = input("Enter your Name :")
bal = int(input("Enter Balance :"))
withdrawl = int(input("Enter money for withdrawal :"))

current_balance = bal

if current_balance < 0:
    print("Invalid Balance")

if current_balance > 0:
    print(f"{current_balance} Rs in your Account")

    if current_balance >= withdrawl:
        current_balance = current_balance - withdrawl
        print("Withdrawal Successfull👍")
        print("Current Balance :",current_balance)
    else:
        print("Balance Insufficient")

else:
    if current_balance == 0:
        print("0 Balance in your Account")



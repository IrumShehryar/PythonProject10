# Program to  simulate ATM

balance = 1000

user_input = (input(" Press 'D' for Deposit, 'W' for Withdrawal, 'C' For checking the balance , exit to quit").upper())


while user_input != "EXIT":
    if user_input == 'D':
        amount=int(input("Enter the amount to deposit"))
        balance += amount
        print("You have deposited", amount ," Rupees in your account")
    elif user_input == 'W':
        amount = int(input("Enter the amount to withdraw"))
        if amount <= balance:
            balance -= amount
            print("You have withdrawn", amount," Rupees from your account")
        else :
            print(" You don't have sufficient balance")
    elif user_input == 'C':
        print("The current balance is", balance)

    else:
        print(" invalid input")
    user_input = input(" Press 'D' for Deposit, 'W' for Withdrawal, 'C' For checking the balance , exit to quit").upper()
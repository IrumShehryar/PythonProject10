# Simple calculator

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y


while True:
    user_input = int(input("Which operation do you want to perform\nPress 1 for Adding\nPress 2 for Subtracting\nPress 3 to Multiple\nPress 4 to Divide\nPress 5 to Exit: "))
    if user_input == 5:
        break
    if user_input == 1 or user_input == 2 or user_input == 3 or user_input ==4 :
        num1 = float(input("Enter value 1: "))
        num2 = float(input("Enter value 2: "))

        if user_input == 1:
            print("The sum of two numbers is:", add(num1,num2))

        elif user_input == 2:
            print("The difference of two numbers is:", subtract(num1, num2))

        elif user_input == 3:
            print("The product of two numbers is:", multiply(num1, num2))

        elif user_input == 4:
            if num2 !=0:
                print("The division of two numbers is:", divide(num1, num2))
            else:
                print("The divisor cannot be 0")

    else :
        print(" Invalid input")
        break


    #user_input = int(input("\nWhich operation do you want to perform\nPress 1 for Adding\nPress 2 for Subtracting\nPress 3 to Multiple\nPress 4 to Divide\nPress 5 to exit"))












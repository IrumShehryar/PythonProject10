"""
3. Make simple Supermarket -program,
• having 10 products with prices in a list as follows:[10,14,22,33,44,13,22,55,66,77].
• asking product number from 1 to 10 and summing its price to totalsum and printing product number and price for every product as in example.
• asking products until user gives '0' to quit the program (while-loop).
• printing  "Total:" and the total sum of prices.
• asking "Payment:" from user and printing "Change:" and finally  calculating and printing the amount of change (payment - totalsum) to customer.
• You must use in this program: while, input

"""
price_list = [10,14,22,33,44,13,22,55,66,77]
totalsum = 0
while True:
    try: # if the user enters invalid numbers ,inform the user to enter only acceptable input
        user_input = int(input("Please select product(1-10) 0 to Quit:"))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10 to select a product or '0' to Quit")
        continue

    if user_input == 0:
        break
    elif 0 < user_input <= 10: # values must lie between 0 and 10
        print("Product: ",user_input,"Price:",price_list[user_input-1])
        totalsum += price_list[user_input-1]
    else:
        print("Invalid input! Please enter a number between 1 and 10")


if totalsum != 0: # if the user quits in the beginning, do not ask for payment and print the change
    print("Total: ",totalsum)
    payment = int(input("Payment: "))
    print("Change: ",payment-totalsum)
else:
    print("See you next time!")
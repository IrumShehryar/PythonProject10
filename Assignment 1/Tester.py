"""
This exercise tests out the default values of parameters. Create a program which has a main function and a sub function called tester.
The main function prompts user for an input "Write something (quit ends): " and sends this input to the sub function as a parameter.
Define the sub function tester so that it has one parameter called "givenstring", which has the default value "Too short". If the user
input is less than 10 characters, the program uses the default value and if 10 or more, it prints the usergiven input. If the user inputs
"quit", the program is terminated.
"""


def tester(givenstring="Too short"):
    print(givenstring)


while True:
    user_input = input("Write something (quit ends):")
    if user_input.lower().strip()=='quit':
        break
    else:
        if len(user_input) < 10:
            tester()
        else:
            tester(user_input)


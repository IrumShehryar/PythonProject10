"""
2. In the second exercise the idea is to create a small grocery shopping list with the list data structure. In short, create a program
that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit. If the user adds something to the
list, the program asks "What will be added?: " and saves it as the last item in the list. If the user decides to remove something, the program
informs the user about how many items there are on the list (There are [number] items in the list.") and prompts the user for the removed item
("Which item is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the final list is printed for the user
"The following items remain in the list:" followed by the remaining items one per line. If the user selects anything outside the options,
including when deleting items, the program responds "Incorrect selection."
"""

shopping_list = []
while True:
    user_input = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?:"))
    if user_input == 1:
        item = input("What will be added?:")
        shopping_list.append(item)
    elif user_input == 2:
        print("There are",len(shopping_list),"items in the list.")
        index=int(input("Which item is deleted?:"))
        if index > len(shopping_list):
            print("Incorrect selection.")
        else:
            shopping_list.pop(index)
    elif user_input == 3:
        print("The following items remain in the list:")
        for i in range(len(shopping_list)):
            print(shopping_list[i])
        break
    else :
        print("Incorrect selection.")

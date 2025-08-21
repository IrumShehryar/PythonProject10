"""
4. In this exercise create two functions
my_split : which splits sentence given as first argument using second argument as a separator character to separate list items.
Function returns a list of items.

my_join : which joins list given as first argument to a string separated with character given as second argument. Function returns a string.
In this exercise you are not allowed to use Python split and join functions

"""
items = []

def my_split(sentence,separator):

    sub_string = ""

    for character in sentence:
        if character != separator:
            sub_string += character

        else:
            items.append(sub_string)
            sub_string = ""
            #print("item=",items)

    if sub_string:
        items.append(sub_string)
    return items

def my_join(string_list,separator):
    sub_string = ""
    for i in range(len(string_list)):
        sub_string += string_list[i]
        if i < len(string_list)-1:
            sub_string += separator
            # print(sub_string)
    return sub_string



sentence = input("Please enter the sentence: ")
split_sentence= my_split(sentence," ")
joined_sentence= my_join(split_sentence,",")

print(joined_sentence)
for word in split_sentence:
    print(word)
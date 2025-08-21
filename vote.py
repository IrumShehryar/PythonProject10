# Program to grant vote casting rights based upon age

age = int(input("Enter age"))
citizenship = input("Are you a citizen? Enter True/False").upper()
#print("age is \n citizenship", age,citizenship)

if citizenship != 'TRUE' and age >= 18:
   print(" You cannot vote , as you are not a citizen")
else :
    if citizenship == 'TRUE' and age > 18:
        print("You can vote")
    else:
        difference = 18 -age
        print(" you are under 18 ,you have to wait for ",difference,"years")





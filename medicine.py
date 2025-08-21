#program to administer medicine based upon patients age

age = int(input("Enter age"))
#print("Age", age)
if  age <15:
    print("The medicine cannot be given")

elif  15 <=age < 18:
    weight = int(input("Enter weight"))
    if weight >= 55:
        print(" The medicine can be given")
    else:
        print(" You are underweight ,the medicine cannot be given")
else:
    print("The medicine can be given")








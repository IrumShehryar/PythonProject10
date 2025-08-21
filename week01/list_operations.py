# Practice with list operations

names = []
names.append("Irum")
print(names)
names.append("Saba")
print(names)
names.insert(2,"Shehryar")
print(names)
names.remove("Shehryar")
print(names)
otherNames = ["Allu","Channay"]
names.extend(otherNames)
print(names)
what_index = names.index("Allu")
print(what_index)
if "Irum" in names:
    print("Irum found")
if "Shehryar" not in names:
    print("Shehryar not found")
names.sort()
print(names)


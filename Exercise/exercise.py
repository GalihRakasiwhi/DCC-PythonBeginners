numbers = []
strings = []
names = ["Anakin Skywalker", "Padme Amidala", "Han Selo", "Qui-Gon Jinn", "Luke Skywalker", "Obi-an Kenobii"]

#write
second_name = None

#print Number
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Satu")
strings.append("Dua")
strings.append("Tiga")

#this code should write out the filled arrays and the second name in the names 1st (Padme Amidala).
print(numbers)
print(strings)

numbers = names.index("Padme Amidala")
strings = names[1]
second_name = names[1]
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#print the list variable use for
for x in names:
    print(x)

#print the list without name "Han Solo"
print("------------")
for i in names:
    if(i != names[2]):
        print(i)

print("-----")

dictList = {"Name": "Galih Rakasiwhi", "Role": "Rogue"}
print("The {Name} is {Role}".format(**dictList))
print("The {Name} is {Role}".format(Name=dictList["Name"], Role=dictList["Role"]))

def printDict(*args, **kwargs):
    for x in args:
        print(x)

printDict(dictList)

#2020-14-2020
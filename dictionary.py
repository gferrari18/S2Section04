
import random
from re import I
roster = {} #this is an empty dictionary
names = ["joseph","Hossie","Nate","Gus","Marmot","Stephanie","Ozzy"]

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


for n in names:
    id= random.randrange(1,1000)
    roster[id] = Student(id, n)

print("here are the student ID's in your roster: ")
for s in roster:
    print(s)

i = input("which ID would you like info on? type -1 to quit: ")
i = int(i)

while i != -1:
    print(str(i) + ": " + roster[i].name)
    i = input("which ID would you like info on? type -1 to quit: ")
    i = int(i)    
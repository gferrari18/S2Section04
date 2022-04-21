import collections
import random
from re import X


class Shopper:
    def __init__(self, name):
        self.name = name


line = collections.deque()

names = ["joseph","Hossie","Nate","Gus","Marmot","Stephanie","Ozzy"]

for l in range(0,100):

    if len(line) < 3:
        person = names[random.randrange(0, len(names))]
        print(person + " have joined the line.")
        line.append(Shopper(person))
    if len(line) > 6:
        x = line.pop()
        print(x.name + " have left the line... impatient")

    i = random.randrange(0,3)
    if i == 0:
        x = line.popleft()
        print("The clerk is now seeing " + x.name)
    else:
        person = names[random.randrange(0, len(names))]
        print(person + " have joined the line.")
        line.append(Shopper(person))



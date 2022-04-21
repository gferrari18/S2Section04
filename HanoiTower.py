import collections

class Stack:
    def __init__(self):
        self.deque = collections.deque()
    
    def push(self, item):
        self.deque.appendleft(item)

    def pop(self):
        return self.deque.popleft()

    def top(self):
        return self.deque[0]

    def len(self):
        return len(self.deque)


s1 = Stack()
s2 = Stack()
s3 = Stack()

s1.push("large")
s1.push("medium")
s1.push("small")

disk = s1.top()
s1.pop()
s3.push(disk)

print(disk + " removed from tower 1 and added to tower 3")

disk = s1.top()
s1.pop()
s2.push(disk)

print(disk + " moved from tower 1 to tower 2")

disk = s3.top()
s3.pop()
s2.push(disk)

print(disk + " moved from tower 3 to tower 2")

disk = s1.top()
s1.pop()
s3.push(disk)

print(disk + " moved from tower 1 to tower 3")

disk = s2.top()
s2.pop()
s1.push(disk)

print(disk + " removed from tower 2 and added to tower 1")

disk = s2.top()
s2.pop()
s3.push(disk)

print(disk + " removed from tower 2 and added to tower 3")

disk = s1.top()
s1.pop()
s3.push(disk)

print(disk + " moved from tower 1 to tower 3")

for x in s3.deque:
    print(x)

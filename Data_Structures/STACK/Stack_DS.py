'''
STack Data Structure
'''

class stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


mystack = stack()
mystack.push("A")
mystack.push("B")
print(mystack.get_stack())
mystack.push("C")
print(mystack.get_stack())
mystack.pop()
print(mystack.get_stack())
mystack.push("2")
mystack.push("4")
print(mystack.is_empty())
print(mystack.peek())
print(mystack.get_stack())

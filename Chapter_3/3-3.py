'''
Imagine a (literal) stack of plates. If the stack gets too high, 
it might topple. Therefore, in real life, we would likely start 
a new stack when the previous stack exceeds some threshold. 
Implement a data structure SetOfStacks that mimics this. 
SetOfStacks should be composed of several stacks and should 
create a new stack once the previous one exceeds capacity. 
SetOfStacks. push() and SetOfStacks. pop() should behave 
identically to a single stack (that is, pop() should return the 
same values as it would if there were just a single stack)

Implement a function popAt(int index) which performs a pop operation on
a specific sub-stack.
'''

class Stack:
    # Initalize the "items" stack
    def __init__(self, size):
        self.size = size
        self.items = []

    # add a new element to the top of the stack
    def push(self, item):
        if len(self.items) and (len(self.items[-1]) < self.size):
            self.items[-1].append(item)
        else:
            self.items.append([item])

    def pop(self):
        while len(self.items) and len(self.items[-1]) < self.size:
            self.items.pop()

        if len(self.items) == 0:
            return  None
        item = self.items[-1].pop()
        if len(self.items[-1]) == 0:
            self.items.pop()
        return item

    def pop_at(self, idx):
        if idx < 0 or len(self.items) <= idx:
            return None
        if len(self.items[idx]) == 0:
            return None
        return self.items[idx].pop()


s = Stack(3)

s.push(4)
s.push(2)
s.push(1)
s.push(5)
s.push(3)

print( s.pop_at(0) )
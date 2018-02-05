'''
Implement a MyQueue class which implements a queue using 
    two stacks.
'''

class Stack:
    # Initalize the "items" stack
    def __init__(self):
        self.items = []

    # add a new element to the top of the stack
    def push(self, item):
        self.items.append(item)

    # remove an element from the top of the stack
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return "Stack Empty"

    # check if the stack is empty or not
    def isEmpty(self):
        return self.items == [ ]

    # traverse stack list
    def traverse(self):
        return self.items


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    # add a new element to the top of the Queue
    def enqueue(self , item):
        while not self.stack1.isEmpty():
            self.stack2.push( self.stack1.pop() )

        self.stack1.push( item )

        while not self.stack2.isEmpty():
            self.stack1.push( self.stack2.pop() )

    # remove an element from the top of the Queue
    def dequeue(self):
        return self.stack1.pop()

    # traverse queue list
    def traverse(self):
        return self.stack1.traverse()


q = MyQueue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)

print( q.traverse() )

q.dequeue()

print( q.traverse() )
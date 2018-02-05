'''
How would you design a stack which, in addition to push and pop, 
also has a function min which returns the minimum element? 
Push, pop and min should all operate in O(1) time
'''
from Chapter_2.Node import Node


class Stack:
    def __init__(self):
        self._min = None
        self.head = None

    def push(self, data):
        if self._min and (self._min.getData() < data):
            old_min = self._min
            self._min = Node ( self._min.getData() )
            self._min.setNext( old_min )
        else:
            old_min = self._min
            self._min = Node ( data )
            self._min.setNext( old_min )

        old_h = self.head
        self.head = Node ( data )
        self.head.setNext( old_h )

    def pop(self):
        if not self.head:
            return "Stack is already empty!"

        self._min = self._min.getNext()
        item = self.head.getData()
        self.head = self.head.getNext()

        return item

    def min(self):
        if not self._min:
            return None

        return self._min.getData()


s = Stack()

s.push(4)
s.push(2)
s.push(1)
s.push(5)
s.push(3)

print( s.min() )
'''
Write a program to sort a stack in ascending order 
(with biggest items on top).
You may use at most one additional stack to hold items, 
but you may not copy the elements into any other data structure 
(such as an array). The stack supports
the following operations: push, pop, peek, and isEmpty.
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

    # retrieve the top element of the stack without remove it
    def peek(self):
        return self.items[ -1 ]

    # traverse stack list
    def traverse(self):
        return self.items


def sort_stack(st):
    ans = Stack()

    while not st.isEmpty():
        tmp = st.pop()
        while not ans.isEmpty() and ans.peek() > tmp:
            st.push( ans.pop() )

        ans.push( tmp )

    return ans



s = Stack()

s.push(4)
s.push(2)
s.push(1)
s.push(5)
s.push(3)

print( s.traverse() )

new_s = sort_stack(s)

print( new_s.traverse() )
'''
    This Stack DS implmentation its follow LIFO [Last-In-First-Out]
    Technique 
'''

from Chapter_2.Node import Node

# Using Lists
class Stack:
    # Initalize the "items" stack
    def __init__(self):
        self.items = []

    # check if the stack is empty or not
    def isEmpty(self):
        return self.items == []

    # return the length of the stack
    def size(self):
        return len(self.items)

    # add a new element to the top of the stack
    def push(self, item):
        self.items.append(item)

    # remove an element from the top of the stack
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return "Stack Empty"

    # retrieve the top element of the stack without remove it
    def peek(self):
        return self.items[ -1 ]

    # traverse stack list
    def traverse(self):
        return self.items

    # reverse the stack
    def reverse(self):
        return self.items[::-1]


# Using LinkedList
class LStack:
    def __init__(self):
        self.head = None

    # add new item to stack
    def push(self, data):
        new_node = Node( data )
        new_node.setNext( self.head )
        self.head = new_node

    # remove last inserted element from stack
    def pop(self):
        if self.isEmpty():
            return "Stack is already empty!"

        tmp = self.head
        self.head = self.head.getNext()
        return tmp.getData()

    # peek function to return top element in stack
    def peek(self):
        return self.head.getData()

    # Check if stack empty or not
    def isEmpty(self):
        return not self.head

    # this to reverse the list
    def reverse(self):
        """
            :return: void, doesn't return anything it reverse list in-place
        """
        current = self.head
        prev = None
        nex = current.getNext ( )
        while current:
            current.setNext ( prev )

            prev = current
            current = nex
            if nex:
                nex = nex.getNext ( )

        self.head = prev

    # This to traverse stack
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.getData())
            current = current.getNext()

        return  elements

    # this to find the size of list
    def size(self):
        """
            :rtype: return the length of list
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext ( )

        return count

    # This to search for specific item and return True if exist False otherwise
    def search(self , item):
        """
            :type value: item [int, string .. etc]
            :rtype: Boolean, return True if item exist otherwise return False
        """
        # if not isinstance(item, Node):
        #     item = Node(item)

        current = self.head
        while current:
            if current.getData ( ) == item:
                return True
            current = current.getNext ( )

        return False
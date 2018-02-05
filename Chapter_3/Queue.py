'''
    This Queue DS implmentation its follow FIFO [First-In-First-Out]
    Technique 
'''
from Chapter_2.Node import Node

# Using Lists
class Queue:
    # Initalize the "items" Queue
    def __init__(self):
        self.items = []

    # check if the Queue is empty or not
    def isEmpty(self):
        return self.items == []

    # return the length of the Queue
    def size(self):
        return len(self.items)

    # add a new element to the top of the Queue
    def enqueue(self, item):
        self.items = [item] + self.items

    # remove an element from the top of the Queue
    def dequeue(self):
        if len(self.items) > 0:
            tmp = self.items[0]
            self.items = self.items[1:]
            return tmp
        return "Queue Empty"

    # traverse queue list
    def traverse(self):
        return self.items

    # reverse the queue
    def reverse(self):
        return self.items[::-1]


# Using Linked List
class LQueue:
    def __init__(self):
        self.head = None

    # This to enqueue element in the first of queue
    def enqueue(self, data):
        new_node = Node( data )
        if self.head:
            curr = self.head
            prev = None
            while curr:
                prev = curr
                curr = curr.getNext()

            prev.setNext( new_node )
        else:
            self.head = Node( data )

    # remove the first elemen in queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is already empty"
        removed_data = self.head.getData()

        if not self.head.getNext():
            self.head = None
        else:
            self.head = self.head.getNext()

        return removed_data

    # check if queue is empty
    def isEmpty(self):
        return not self.head

    # traverse all elements in queue
    def traverse(self):
        elements = []
        curr = self.head
        while curr:
            elements.append( curr.getData() )
            curr = curr.getNext()

        return elements

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

    # this to find the size of queue
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

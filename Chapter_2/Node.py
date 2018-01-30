
'''
    This class to define Node class for Single and double linked list
'''

# For Single linked list
class Node:
    # Initalize node with data and next reference
    def __init__(self, data):
        self.data = data
        self.next = None

    # this value to return node data
    def getData(self):
        return self.data

    # this to set current node data
    def setData(self, new_data):
        self.data = new_data

    # This to get next node for current node
    def getNext(self):
        return self.next

    # This to set next node fir current node
    def setNext(self, next_node):
        self.next = next_node

# For Double linked list
class DNode:
    # Initalize node with data and next reference
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    # this value to return node data
    def getData(self):
        return self.data

    # this to set current node data
    def setData(self, new_data):
        self.data = new_data

    # This to get next node for current node
    def getNext(self):
        return self.next

    # This to set next node fir current node
    def setNext(self, next_node):
        self.next = next_node

    # This to get prev node for current node
    def getPrev(self):
        return self.prev

    # This to set prev node for current node
    def setPrev(self, prev_node):
        self.prev = prev_node
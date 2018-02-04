'''
    This class to implment :
    SingleLinkedList:
        1- UnorderedList Contains:
                1-  isEmpty()
                2-  push()
                3-  append()
                4-  size()
                5-  search()
                6-  searchPos()
                7-  findByPos()
                8-  remove()
                9-  pop() the last node
                10- popByPos() by pos
                11- traverse()
                12- reverse()

        2- OrderedList Contains:
                1-  isEmpty()
                2-  add()
                3-  size()
                4-  search()
                5-  index()
                6-  findByPos()
                7-  remove()
                8-  pop()  the last node
                9-  popByPos()  by node pos
                10- traverse()
                11- reverse()
    using Node class
'''

# from Node import Node
from Chapter_2.Node import Node


class UnorderedList:
    # initalize the list with head = None
    def __init__(self):
        """
                UnorderedList Contains:
                    1-  isEmpty()
                    2-  push()
                    3-  append()
                    4-  size()
                    5-  search()
                    6-  searchPos()
                    7-  findByPos()
                    8-  remove()
                    9-  pop() the last node
                    10- popByPos() by pos
                    11- traverse()
                    12- reverse()
        """
        self.head = None

    # This to check if list is empty or not
    def isEmpty(self):
        """
            :rtype: Boolean, return true of false
        """
        return self.head == None

    # This to add an item at the first on list
    def push(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: void Do not return anything, just add node in the first of list
        """
        # if not isinstance(item, Node):
        item = Node(item)

        item.setNext(self.head)
        self.head = item

        return

    # This to add an item to the end
    def append(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: void Do not return anything, just add node in the end of list
        """
        item = Node(item)

        current = self.head
        while current:
            if not current.getNext():
                break
            current = current.getNext()

        if current:
            current.setNext(item)
        else:
            self.head = item

        item.setNext(None)

        return

    # this to find the size of list
    def size(self):
        """
            :rtype: return the length of list
        """
        current = self.head
        count = 1
        while current:
            count += 1
            current = current.getNext()

        return count

    # This to search for specific item and return True if exist False otherwise
    def search(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: Boolean, return True if item exist otherwise return False
        """
        # if not isinstance(item, Node):
        #     item = Node(item)

        current = self.head
        while current:
            if current.getData() == item:
                return True
            current = current.getNext()

        return False

    # This search for specific item and return it's position otherwise return -1
    def index(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: int, the node position in list or -1 if not in it
        """
        # if not isinstance(item, Node):
        #     item = Node(item)

        current = self.head
        pos = 1
        while current:
            if current.getData() == item:
                return pos
            pos += 1
            current = current.getNext()

        return -1

    # This to find an element at specific position and return it's data or -1 if nposition is wrong
    def findByPos(self, pos):
        """
            :type pos: the node position which you looking for
            :rtype: node data, return node.data when find its position or -1 if pos is wrong
        """
        current = self.head
        current_pos = 1
        while current:
            if current_pos == pos:
                return current.getData()
            current = current.getNext()
            current_pos += 1

        return -1

    # This to remove specifc node from list
    def remove(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: Boolean, if node deleted return True otherwise return False
        """
        # if not isinstance(item, Node):
        #     item = Node(item)

        current = self.head
        prev = None
        while current:
            if current.getData() == item:
                if prev:
                    prev.setNext( current.getNext() )
                else:
                    self.head = current.getNext()

                return True
            prev = current
            current = current.getNext()

        return False

    # This to traverse all list nodes and collect them in list
    def traverse(self):
        """
            :rtype: list, list of nodes in your list
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(current.getData())
            current = current.getNext()

        return nodes

    # this pop function to remove the last elment and return it
    def pop(self):
        """
            :return: node data, the deleted node data which it's last node
        """
        current = self.head
        prev = None
        while current:
            if not current.getNext():
                if prev:
                    prev.setNext(None)
                else:
                    self.head = None
                return current.getData()
            prev = current
            current = current.getNext()

        return

    # this pop function to remove exact item in exact pos
    def popByPos(self, pos):
            """
            :param pos: it's an integer value specfied the wanted node to delete pos
            :return: node data, the deleted node data which it's last node
            """
            current = self.head
            prev = None
            current_pos = 1
            while current:
                if current_pos == pos:
                    if prev:
                        prev.setNext(current.getNext())
                    else:
                        self.head = current.getNext()
                    return current.getData()
                prev = current
                current = current.getNext()
                current_pos += 1

            return

    # this to reverse the list
    def reverse(self):
        """
            :return: void, doesn't return anything it reverse list in-place
        """
        current = self.head
        prev = None
        nex = current.getNext()
        while current:
            current.setNext(prev)

            prev = current
            current = nex
            if nex:
                nex = nex.getNext()

        self.head = prev

    # This function to remove Duplcates from list using Hashing
    def removeDuplicates(self):
        """
        :return: Void, just remove duplicates and return nothing 
        """
        visited = {}
        current = self.head
        prev = None
        current_pos = 1
        while current:
            if current.getData() in visited:
                self.popByPos(current_pos)
                # if prev:
                #     prev.setNext ( current.getNext ( ) )
                # else:
                #     self.head = current.getNext ( )
                current = current.getNext()
                continue
            else:
                visited[current.getData()] = True
            prev = current
            current = current.getNext()
            current_pos += 1

    # This function to partition list around x, less than x before ones which greater or equal to x
    def partition(self, x):
        """
            Initialize first and last nodes of three linked lists
                1) Linked list of values smaller than x.
                2) Linked list of values equal to x.
                3) Linked list of values greater than x.
        :param x: node data 
        :return:  void
        """
        smaller_h, smaller_l = None, None
        equal_h , equal_l = None , None
        greater_h , greater_l = None , None

        # iterate original list and connect nodes of appropriate linked lists.
        while self.head:
            # If current node is equal to x, append it to the list of x values
            if self.head.getData() == x:
                if not equal_h:
                    equal_h = equal_l = self.head
                else:
                    equal_l.setNext( self.head )
                    equal_l = equal_l.getNext()
            # If current node is less than X, append it to the list of smaller values
            elif self.head.getData() < x:
                if not smaller_h:
                    smaller_h = smaller_l = self.head
                else:
                    smaller_l.setNext( self.head )
                    smaller_l = self.head
            # Append to the list of greater values
            else:
                if not greater_h:
                    greater_h = greater_l = self.head
                else:
                    greater_l.setNext( self.head )
                    greater_l = self.head

            self.head = self.head.getNext()

        # Fix end of greater linked list to NULL if this  greater list has nodes
        if not greater_h:
            greater_l.setNext( None )

        # If smaller list is empty
        if not smaller_h:
            if not equal_h:
                    self.head = greater_h
                    return
            equal_l.setNext( greater_h )
            self.head = equal_h
            return
        # If smaller list is not empty and equal list is empty
        if not equal_h:
            smaller_l.setNext( greater_h )
            self.head = smaller_h
            return

        # if both smaller and equal lists not empty
        smaller_l.setNext( equal_h )
        equal_l.setNext( greater_h )
        self.head = smaller_h
        return

    # this to sort list in asc order
    def sort(self):
        current = self.head

        while True:
            got_sorted = False
            while current:
                try:
                    if current.getData() > current.getNext().getData():
                        temp_data = current.getData()
                        current.setData( current.getNext().getData() )
                        current.getNext().setData( temp_data )
                        got_sorted = True

                except AttributeError:
                    pass

                current = current.getNext()

            if got_sorted == False:
                break
            else:
                current = self.head

    # tis to find the start of looping in list
    def findStartOfLoop(self):
        """
        :return: node data 
        """
        nodes = {}
        current = self.head
        while current:
            if current.getData() in nodes:
                return current.getData()
            nodes[current.getData()] = True
            current = current.getNext()

        return None

class OrderedList:
    # initalize the list with head = None
    def __init__(self):
        """
            OrderedList Contains:
                1-  isEmpty()
                2-  add()
                3-  size()
                4-  search()
                5-  index()
                6-  findByPos()
                7-  remove()
                8-  pop()  the last node
                9-  popByPos()  by node pos
                10- traverse()
                11- reverse()
        """
        self.head = None

    # This to check if list is empty or not
    def isEmpty(self):
        """
            :rtype: Boolean, return true of false
        """
        return self.head == None

    # This to add node to list
    def add(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: void Do not return anything, just add node in its sutiable position
        """
        current = self.head
        prev = None
        # stop = False
        while current:
            if current.getData() > item:
                break
            else:
                prev = current
                current = current.getNext()
        new_node = Node(item)
        if not prev:
            new_node.setNext(self.head)
            self.head = new_node
        else:
            new_node.setNext(current)
            prev.setNext(new_node)

        return

    # this to find the size of list
    def size(self):
        """
            :rtype: return the length of list
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()

        return count

    # This to search for specific item and return True if exist False otherwise
    def search(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: Boolean, return True if item exist otherwise return False
        """
        # if not isinstance(item, Node):
        #     item = Node(item)

        current = self.head
        while current:
            if current.getData() == item:
                return True
            else:
                if current.getData() > item:
                    return False
                else:
                    current = current.getNext()

        return False

    # This search for specific item and return it's position otherwise return -1
    def index(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: int, the node position in list or -1 if not in it
        """
        # if not isinstance(item, Node):
        #     item = Node(item)

        current = self.head
        pos = 1
        while current:
            if current.getData() == item:
                return pos
            else:
                if current.getData() > item:
                    return -1
                else:
                    pos += 1
                    current = current.getNext()

        return -1

    # This to find an element at specific position and return it's data or -1 if nposition is wrong
    def findByPos(self, pos):
        """
            :type pos: the node position which you looking for
            :rtype: node data, return node.data when find its position or -1 if pos is wrong
        """
        current = self.head
        current_pos = 1
        while current:
            if current_pos == pos:
                return current.getData()
            current = current.getNext()
            current_pos += 1

        return -1

    # This to remove specifc node from list
    def remove(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: Boolean, if node deleted return True otherwise return False
        """
        # if not isinstance(item, Node):
        #     item = Node(item)

        current = self.head
        prev = None
        while current:
            if current.getData() == item:
                if prev:
                    prev.setNext(current.getNext())
                else:
                    self.head = current.getNext()

                return True
            prev = current
            current = current.getNext()

        return False

    # This to traverse all list nodes and collect them in list
    def traverse(self):
            """
                :rtype: list, list of nodes in your list
            """
            nodes = []
            current = self.head
            while current:
                nodes.append(current.getData())
                current = current.getNext()

            return nodes

    # this pop function to remove the last elment and return it
    def pop(self):
        """
            :return: node data, the deleted node data which it's last node
        """
        current = self.head
        prev = None
        while current:
            if not current.getNext():
                if prev:
                    prev.setNext(None)
                else:
                    self.head = None
                return current.getData()
            prev = current
            current = current.getNext()

        return

    # this pop function to remove exact item in exact pos
    def popByPos(self, pos):
        """
        :param pos: it's an integer value specfied the wanted node to delete pos
        :return: node data, the deleted node data which it's last node
        """
        current = self.head
        prev = None
        current_pos = 1
        while current:
            if current_pos == pos:
                if prev:
                    prev.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                return current.getData()
            prev = current
            current = current.getNext()
            current_pos += 1

        return

    # this to reverse the list
    def reverse(self):
        """
            :return: void, doesn't return anything it reverse list in-place
        """
        current = self.head
        prev = None
        nex = current.getNext()
        while current:
            current.setNext(prev)

            prev = current
            current = nex
            if nex:
                nex = nex.getNext()

        self.head = prev

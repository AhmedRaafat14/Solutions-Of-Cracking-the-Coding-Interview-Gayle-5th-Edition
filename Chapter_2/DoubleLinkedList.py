"""
    This class to implment :
        DoubledLinkedList contains:
                1-  isEmpty()
                2-  push()
                3-  append()
                4-  insertBefore()
                5-  insertAfter()
                6-  size()
                7-  isExist()
                8-  index()
                9-  findByPos()
                10- findBeforePos()
                11- findAfterPos()
                12- remove()
                13- pop()
                14- popByPos()
                16- Traverse()
"""

# from Node import DNode as Node
from Chapter_2.Node import DNode as Node

class DoubleLinkedList:
    def __init__(self):
        """
            DoubledLinkedList contains:
                1-  isEmpty()
                2-  push()
                3-  append()
                4-  insertBefore()
                5-  insertAfter()
                6-  size()
                7-  isExist()
                8-  index()
                9-  findByPos()
                10- findBeforePos()
                11- findAfterPos()
                12- remove()
                13- pop()
                14- popByPos()
                16- Traverse()
        """
        self.head = None

    # this to check if list is empty or not
    def isEmpty(self):
        """
        :return: Bolean, return True if list empty False if it has data
        """
        return self.head == None

    # This to add item to the start of list
    def push(self, item):
        """
        :param item: it's an new node data
        :return:  void doesn't return anything
        """
        item = Node(item)

        if self.head:
            self.head.setPrev(item)
        item.setNext(self.head)
        item.setPrev(None)
        self.head = item

    # this to add item to the end of list
    def append(self, item):
        """
        :param item: it's an new node data
        :return: void doesn't return anything
        """
        current = self.head

        while current:
            if not current.getNext():
                break
            current = current.getNext()

        if not self.head:
            item = Node(item)
            self.head = item
        else:
            item = Node(item)
            current.setNext(item)
            item.setPrev(current)
            item.setNext(None)

    # This insert node before specific pos
    def insertBefore(self, pos, item):
        """
        :param pos: int, to specify the pos of new element
        :param item: data, the new node data value
        :return: Bolean, True if insertion succeded False otherwise
        """
        item = Node(item)
        current = self.head
        prev = None

        current_pos = 1
        while current:
            if current_pos == pos:
                if prev:
                    prev.setNext(item)
                    item.setPrev(prev)
                    item.setNext(current)
                    current.setPrev(item)
                else:
                    self.head.setPrev(item)
                    item.setNext(self.head)
                    item.setPrev(None)
                    self.head = item
                return True
            prev = current
            current = current.getNext()
            current_pos += 1
        return False

    # This to insert node after specific pos
    def insertAfter(self, pos, item):
        """
        :param pos: int, to specify the pos of new element
        :param item: data, the new node data value
        :return: Bolean, True if insertion succeded False otherwise
        """
        if pos <= 1:
            return "Pos must be greater than or equal to one"
        item = Node(item)
        current = self.head
        nxt = current.getNext()

        current_pos = 1
        while current:
            if current_pos == pos:
                if nxt:
                    nxt.setPrev(item)
                    current.setNext(item)
                    item.setNext(nxt)
                    item.setPrev(current)
                else:
                    if current_pos > 1:
                        item.setPrev(current)
                        item.setNext(nxt)
                        current.setNext(item)
                    else:
                        item.setNext(self.head.getNext())
                        item.setPrev(self.head.getPrev())
                        self.head.setPrev(item)

                        self.head = item
                return True
            current = current.getNext()
            nxt = current.getNext()
            current_pos += 1
        return False

    # this to find the length of list
    def size(self):
        """
        :return:    int, the size of list
        """
        current = self.head
        count = 1
        while current:
            count += 1
            current = current.getNext()

        return count

    # this to check if the item exist or not
    def isExist(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: Boolean, return True if item exist otherwise return False
        """
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

        return None

    # This to find the node which exist before specified pos
    def findBeforePos(self, pos):
        """
        :param pos: int, specify the node pos which we want to get the prev node for it
        :return: node data, the node data
        """
        current = self.head
        current_pos = 1
        while current:
            if current_pos == pos:
                if not current.getPrev():
                    return None
                founded = current.getPrev()
                return founded.getData()
            current = current.getNext()
            current_pos += 1

        return None

    # This to find the node which exist after specified pos
    def findAfterPos(self, pos):
        """
        :param pos: int, specify the node pos which we want to get the next node for it
        :return: node data, the node data
        """
        current = self.head
        current_pos = 1
        while current:
            if current_pos == pos:
                if not current.getNext():
                    return None
                return current.getNext().getData()
            current = current.getNext()
            current_pos += 1

        return None

    # This to remove specific element in list
    def remove(self, item):
        """
        :param item: node data, which we want to remove it
        :return: return True if deleted and False if not
        """
        current = self.head
        prev = current.getPrev()
        while current:
            if current.getData() == item:
                if prev:
                    prev.setNext(current.getNext())
                    if current.getNext():
                        current.getNext().setPrev(prev)
                    else:
                        current.setPrev(None)
                else:
                    self.head = current.getNext()
                    current.setPrev(None)
                return True
            prev = current
            current = current.getNext()

        return False

    # This to remove last element and return its data
    def pop(self):
        """
        :return: node data, return deleted node data
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

        return None

    # This to remove specific node at specific pos
    def popByPos(self, pos):
        """
        :param pos: int value, specify the position of wanted element to delete
        :return: node data, return deletd node data
        """
        current = self.head
        current_pos = 1
        prev = None
        while current:
            if current_pos == pos:
                if prev:
                    # set previous node next pointer to deleted node next
                    prev.setNext(current.getNext())
                    # set to the next of deleted node prev pointer to prev node
                    if current.getNext():
                        current.getNext().setPrev(prev)
                    else:
                        current.setPrev(None)
                else:
                    self.head = current.getNext()
                    current.setPrev(None)
                return current.getData()
            prev = current
            current = current.getNext()
            current_pos += 1

        return None

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
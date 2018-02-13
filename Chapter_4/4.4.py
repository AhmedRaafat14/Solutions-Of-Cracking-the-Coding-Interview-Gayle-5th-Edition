class Node:
    # Initalize node with data and next reference
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # initalize the list with head = None
    def __init__(self):
        self.head = None
    # This to add an item to the end
    def append(self, item):
        """
            :type value: item [int, string .. etc]
            :rtype: void Do not return anything, just add node in the end of list
        """
        item = Node(item)

        current = self.head
        while current:
            if not current.next:
                break
            current = current.next

        if current:
            current.next = item
        else:
            self.head = item

        item.next = None

        return

    # This to traverse all list nodes and collect them in list
    def traverse(self):
        """
            :rtype: list, list of nodes in your list
        """
        nodes = [ ]
        current = self.head
        while current:
            nodes.append ( current.data )
            current = current.next

        return nodes

class BinaryTree:
    def __init__(self, val):
        self.data = val
        self.left_child = None
        self.right_child = None

    # insert node to left of some node
    def insert_left(self , data):
        if not self.left_child:
            self.left_child = BinaryTree ( data )
        else:
            new_node = BinaryTree ( data )
            new_node.left_child , self.left_child = self.left_child , new_node

        return

    # insert node to the right of some node
    def insert_right(self , data):
        if not self.right_child:
            self.right_child = BinaryTree ( data )
        else:
            new_node = BinaryTree ( data )
            new_node.right_child , self.right_child = self.right_child , new_node

        return

    def constructLinkedLists(self):
        # TO hold current level nodes works as queue
        currentLevel = [self]
        # to hold levels linked lists
        lists = []
        # will iterate till we finish tree whc=ich will make currentlevel empty
        while currentLevel:
            # this will hold next level nodes to assign them
            #   in next iteration to currentLevel list
            nextLevel = []
            # level list just work as temp linked list to hold
            #    each level linked list constructd=s from this level nodes
            level_list = LinkedList()
            # we use queue here in bfs traverse queue will hold each
            #  level in tree nodes in it, so use this feature to iterate
            #  over this nodes and constrct a linked list objects use them
            for n in currentLevel:
                # appedn to linked list new node
                level_list.append( n.data )
                # if this node has childs append them to nextLevel
                #  list to work on them in next iteration which will be
                #   a new level
                if n.left_child:
                    nextLevel.append( n.left_child )
                if n.right_child:
                    nextLevel.append( n.right_child )
            # Now, we have a linked list for finished level append it
            #   in our solution list called: lists
            lists.append( level_list )
            # reiterate over currentLevel by new level nodes which filled in nextLevel list
            currentLevel = nextLevel
        return lists


if __name__ == "__main__":
    """
                 1
               /   \
              /     \
             2       5
            / \     / \
           /   \   /   \
          3     4  6    7
    """
    a_n = BinaryTree ( 1 )
    a_n.insert_left ( 2 )
    a_n.insert_right ( 5 )

    b_n = a_n.left_child
    b_n.insert_right ( 4 )
    b_n.insert_left ( 3 )

    c_n = a_n.right_child
    c_n.insert_left ( 6 )
    c_n.insert_right ( 7 )

    lis = a_n.constructLinkedLists ( )

    for l in lis:
        print ( *l.traverse ( ) , sep=' ---- ' )
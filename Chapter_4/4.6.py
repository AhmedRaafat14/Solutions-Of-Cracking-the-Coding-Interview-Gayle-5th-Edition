"""
Write an algorithm to find the'next'node 
(i.e., in-order successor) of a given node in a binary search 
tree. You may assume that each node has a link to its parent
"""

class BinarySearchTree:
    def __init__(self, val):
        self.data = val
        self.left_child = None
        self.right_child = None
        self.parent = None

    # insert new node to right or left of current node
    def insert(self, data):
        if data <= self.data and self.left_child:
            self.left_child.insert(data)
        elif data <= self.data:
            tmp = BinarySearchTree(data)
            tmp.parent = self
            self.left_child  =  tmp
        elif data > self.data and self.right_child:
            self.right_child.insert(data)
        else:
            tmp = BinarySearchTree(data)
            tmp.parent = self
            self.right_child  =  tmp

    # pre-order traversal
    def pre_order(self):
        if not self:
            nodes = []
        nodes = []

        nodes.append(self.data)

        if self.left_child:
            l = self.left_child.pre_order()
            for n in l:
                nodes.append(n)

        if self.right_child:
            r = self.right_child.pre_order()
            for n in r:
                nodes.append(n)

        return nodes

    # this to get the node which equal to user key
    def find(self , data):
        if data < self.data and self.left_child:
            return self.left_child.find ( data )
        if data > self.data and self.right_child:
            return self.right_child.find ( data )

        if data == self.data:
            return self
        return None

# App 1: without parent link
def findNext(root, data):
    node = root.find(data)
    # case 1: if node have a right child so successor of it
    # will be the left most node, so get it and return it
    if node.right_child:
        return left_most_node(node.right_child)

    # case 2: if node doesn't have right child or look for mn val in lef
    # or if it doesn't have right or left childs will go backtracking
    # to parents till we find the largest parent node greater than it.
    next_node = BinarySearchTree('')
    while root:
        if node.data < root.data:
            next_node = root
            root = root.left_child
        elif node.data > root.data:
            root =  root.right_child
        else:
            break

    return next_node.data

# App 2: using parent link
def findNext_2(root, data):
    node = root.find ( data )
    # case 1: if node have a right child so successor of it
    # will be the left most node, so get it and return it
    if node.right_child:
        return left_most_node ( node.right_child )

    # case 2: if node doesn't have right child or look for mn val in lef
    # or if it doesn't have right or left childs will go backtracking
    # to parents till we find the largest parent node greater than it.
    parent = node.parent
    while parent:
        if node.data != parent.right_child.data:
            break
        node = parent
        parent = parent.parent

    return parent.data

def left_most_node(curr):
    while curr:
        if not curr.left_child:
            return curr.data
        curr = curr.left_child

if __name__ == "__main__":
    bst = BinarySearchTree(20)

    bst.insert(8)
    bst.insert(22)
    bst.insert(4)
    bst.insert(12)
    bst.insert(10)
    bst.insert(14)

    # print( *bst.pre_order(), sep='  ' )
    print( "1- Next node for node 20 is :" + str( findNext(bst, 20) ) )
    print ( "1- Next node for node 8 is :" + str ( findNext ( bst , 8 ) ) )
    print ( "1- Next node for node 4 is :" + str ( findNext ( bst , 4 ) ) )
    print ( "1- Next node for node 14 is :" + str ( findNext ( bst , 14 ) ) )
    print("======================================")
    print ( "2- Next node for node 20 is :" + str ( findNext_2 ( bst , 20 ) ) )
    print ( "2- Next node for node 8 is :" + str ( findNext_2 ( bst , 8 ) ) )
    print ( "2- Next node for node 4 is :" + str ( findNext_2 ( bst , 4 ) ) )
    print ( "3- Next node for node 14 is :" + str ( findNext_2 ( bst , 14 ) ) )
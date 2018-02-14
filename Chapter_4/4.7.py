"""
Design an algorithm and write code to find the first common 
ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    # insert node to left of some node
    def insert_left(self, data):
        new_node = BinaryTree ( data )
        new_node.parent = self

        if not self.left_child:
            self.left_child = new_node
        else:
            new_node.left_child, self.left_child = self.left_child, new_node

        return new_node

    # insert node to the right of some node
    def insert_right(self, data):
        new_node = BinaryTree ( data )
        new_node.parent = self

        if not self.right_child:
            self.right_child = new_node
        else:
            new_node.right_child , self.right_child = self.right_child , new_node

        return new_node

    def in_order(self):
        if not self:
            nodes = []

        nodes = []
        if self.left_child:
            l = self.left_child.in_order( )
            for el in l:
                nodes.append(el)

        # print ( self.data )
        nodes.append( self.data )

        if self.right_child:
            r = self.right_child.in_order ( )
            for el in r:
                nodes.append(el)

        return nodes

def findAnc(root, n1, n2):
    if root in (None, n1, n2):
        return root

    left  = findAnc(root.left_child, n1, n2)
    right = findAnc(root.right_child, n1, n2)

    if left and right:
        return root

    return left if left else right

if __name__ == "__main__":
    bt = BinaryTree(1)
    bt_2 = bt.insert_left(2)
    bt_5 = bt.insert_right(5)

    bt_3 = bt_2.insert_left(3)
    bt_4 = bt_2.insert_right(4)

    bt_6 = bt_5.insert_left ( 6 )
    bt_7 = bt_5.insert_right ( 7 )

    # print( *bt.in_order(), sep='  ' )
    print ( findAnc ( bt , bt , bt_2 ).data )


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

    def isBST(self):
        if not self or not self.left_child or not self.right_child:
            return None

        if self.left_child:
            self.left_child.isBST( )

        if self.left_child.data > self.data or self.data >= self.right_child.data:
            return False

        if self.right_child:
            self.right_child.isBST ( )

        return True

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
    a_n = BinaryTree(1)
    a_n.insert_left(2)
    a_n.insert_right(5)

    b_n = a_n.left_child
    b_n.insert_right(4)
    b_n.insert_left(3)

    c_n = a_n.right_child
    c_n.insert_left(6)
    c_n.insert_right(7)

    """
                     5
                   /   \
                  /     \
                 3       8
                / \     / \
               /   \   /   \
              2     4  6    7
    """
    # a_n = BinaryTree ( 5 )
    # a_n.insert_left ( 3 )
    # a_n.insert_right ( 8 )
    #
    # b_n = a_n.left_child
    # b_n.insert_right ( 2 )
    # b_n.insert_left ( 4 )
    #
    # c_n = a_n.right_child
    # c_n.insert_left ( 6 )
    # c_n.insert_right ( 7 )

    print( a_n.isBST() )
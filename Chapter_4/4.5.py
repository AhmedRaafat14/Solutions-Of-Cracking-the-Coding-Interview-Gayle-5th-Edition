"""
Implement a function to check if a binary tree is a binary 
    search tree.
"""

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

    
    def pre_order(self):
        if not self:
            nodes = []
        # print(self.data)
        nodes = []
        if self.left_child:
            l = self.left_child.pre_order( )
            for el in l:
                nodes.append(el)
        
        nodes.append( self.data )
        
        if self.right_child:
            r = self.right_child.pre_order( )
            for el in r:
                nodes.append(el)

        return nodes

def isBST(root, low, high):
        if not root:
            return True
        
        return low <= root.data and high > root.data and \
                    isBST(root.left_child, low, root.data ) and \
                    isBST(root.right_child, root.data, high )

if __name__ == "__main__":
    """
                     4
                   /   \
                  /     \
                 2       6   ===============> True
                / \     / \
               /   \   /   \
              1     3  5    7
              
                     4
                   /   \
                  /     \
                 2       6   ===============> False
                / \     / \
               /   \   /   \
              3     1  5    7
    """
    a_n = BinaryTree(4)
    a_n.insert_left(2)
    a_n.insert_right(6)

    b_n = a_n.left_child
    b_n.insert_left(3)
    b_n.insert_right(1)
#     b_n.insert_left(1)
#     b_n.insert_right(3)

    c_n = a_n.right_child
    c_n.insert_left(5)
    c_n.insert_right(7)
    
    print( *a_n.pre_order(), sep=' ---> ' )
    
    print( isBST(a_n, float('-inf'), float('inf') ) )

"""
Given a sorted (increasing order) array with unique integer 
elements, write an algorithm to create a binary search tree 
with minimal height
"""

class BinarySearchTree:
    def __init__(self, val):
        self.data = val
        self.left_child = None
        self.right_child = None

    def pre_order(self):
        if not self:
            nodes = []

        nodes = []
        nodes.append( self.data )
        # print(self.data)

        if self.left_child:
            l = self.left_child.pre_order( )
            for el in l:
                nodes.append(el)

        if self.right_child:
            r = self.right_child.pre_order( )
            for el in r:
                nodes.append(el)

        return nodes


def convertSortedListToBST(arr):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2

    root = BinarySearchTree( arr[mid] )

    root.left_child  = convertSortedListToBST( arr[:mid] )
    root.right_child = convertSortedListToBST( arr[mid + 1:] )

    return root

bst = convertSortedListToBST( [1, 2, 3, 4, 5, 6, 7] )

print( *bst.pre_order(), sep=' ---->' )
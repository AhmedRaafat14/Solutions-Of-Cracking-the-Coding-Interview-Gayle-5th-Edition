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

###### Approach 1 ############
def convertSortedListToBST_1(arr):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2

    root = BinarySearchTree( arr[mid] )

    root.left_child  = convertSortedListToBST_1( arr[:mid] )
    root.right_child = convertSortedListToBST_1( arr[mid + 1:] )

    return root

###### Approach 2 ############
def convertSortedListToBST_2(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    root = BinarySearchTree( arr[mid] )

    root.left_child  = convertSortedListToBST_2( arr, start, mid - 1 )
    root.right_child = convertSortedListToBST_2( arr, mid + 1, end )

    return root

nums = [1, 2, 3, 4, 5, 6, 7]
bst_1 = convertSortedListToBST_1( nums )
bst_2 = convertSortedListToBST_2(nums, 0, len(nums) - 1)

print( *bst_1.pre_order(), sep=' ---->' )
print( *bst_2.pre_order(), sep=' ---->' )
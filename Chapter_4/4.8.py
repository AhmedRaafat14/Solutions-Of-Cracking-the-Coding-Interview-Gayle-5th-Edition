"""
You have two very large binary trees: Tl, with millions of nodes, 
and T2, with hundreds of nodes. Create an algorithm to decide 
if T2 is a subtree of Tl. A tree T2 is a subtree of Tl if there 
exists a node n in Tl such that the subtree of n is identical to 
T2. That is, if you cut off the tree at node n, 
the two trees would be identical.
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

# App 1: we just get the in_order for both trees and compare them
def T2IsSubOfT1(T1, T2):
    if not T1:
        return False
    T1_in = T1.in_order()
    T2_in = T2.in_order()
    if T2_in[0] not in T1_in:
        return False
    first_t2 = T1_in.index(T2_in[0])
    return T1_in[first_t2: first_t2+len(T2_in) ] == T2_in

# App 2: we go throw big tree till we find root node then we
#      go to check if tree match from here
def isSubTree(T1, T2):
    if not T1:
        return False

    if T1.data == T2.data:
        if matchTree(T1, T2):
            return True

    return isSubTree(T1.left_child, T2) or isSubTree(T1.right_child, T2)

def matchTree(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.data != root2.data:
        return False
    return matchTree(root1.left_child, root2.left_child) and\
           matchTree(root1.right_child, root2.right_child)

if __name__ == "__main__":
    bt = BinaryTree(1)
    bt_2 = bt.insert_left(2)
    bt_5 = bt.insert_right(5)

    bt_3 = bt_2.insert_left(3)
    bt_4 = bt_2.insert_right(4)

    bt_10 = bt_4.insert_left(10)
    bt_11 = bt_4.insert_right ( 11 )

    bt_6 = bt_5.insert_left ( 6 )
    bt_7 = bt_5.insert_right ( 7 )

    btt = BinaryTree(4)
    btt_10 = btt.insert_left(10)
    btt_11 = btt.insert_right(11)

    print( T2IsSubOfT1(bt, btt) )
    print( isSubTree(bt, btt) )


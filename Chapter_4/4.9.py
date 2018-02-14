"""
You are given a binary tree in which each node contains a value. 
Design an algorithm to print all paths which sum to a given value.
The path does not need to start or end at the root or a leaf
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

    def findPath(self, target):
        if not self:
            return []
        l = []
        if self.left_child:
            l = self.left_child.findPath(target)
        r = []
        if self.right_child:
            r = self.right_child.findPath(target)
        return self.getPaths(target) + l + r

    def getPaths(self, target):
        if not self:
            return []
        path = l_left = l_right = []
        if self.data == target:
            path = [[self.data]]

        if self.left_child:
            l_left = self.left_child.getPaths( target - self.data )
            if l_left:
                l_left = [ [self.data] + n for n in l_left ]

        if self.right_child:
            l_right = self.right_child.getPaths ( target - self.data )
            if l_right:
                l_right = [ [ self.data ] + n for n in l_right ]

        return path + l_left + l_right


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

    print( bt.findPath(6) )
'''
Implement a function to check if a binary tree is balanced. 
For the purposes of this question, a balanced tree is defined 
to be a tree such that the heights of the two subtrees of any 
node never differ by more than one
                    
                    12
                  /    \
                 8     16
                /     /  \ 
               4     13  17
'''

class Node:
    # Initalize node with data and next reference
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0  # define balance factor h2 - h1

    def insert(self, data):
        new_node = Node(data)
        # If there's no nodes in tree
        if not self.node:
            self.node       = new_node
            self.node.left  = BinaryTree()
            self.node.right = BinaryTree()
        # if node less than current node value insert in left
        elif data <= self.node.data:
            self.node.left.insert(data)
        # if node greater than current node value insert in right
        elif data > self.node.data:
            self.node.right.insert(data)

    # Approach 2
    def updateHeight(self):
        """
        Update tree height it the longest path from root to fairest
        leaf + 1 
        :return: void
        """
        if self.node:
            if self.node.left:
                self.node.left.updateHeight ( )
            if self.node.right:
                self.node.right.updateHeight ( )

            self.height = 1 + max ( self.node.left.height , self.node.right.height )
        else:
            self.height = -1

    def updateBalance(self):
        """
        this to calculate the node balance factor by :
        factor = height(left sub tree) - height(right sub tree)
        :return: void
        """
        if self.node:
            if self.node.left:
                self.node.left.updateBalance()
            if self.node.right:
                self.node.right.updateBalance()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def checkBalanced(self):
        if not self or not self.node:
            return True

        return ( (abs ( self.balance ) < 2) and self.node.left.checkBalanced ( ) and self.node.right.checkBalanced ( ) )

    ###### Approache 2 Efficient one
    def checkHeight(self):
        if not self.node:
            return 0
        left_h = self.node.left.checkHeight()
        if left_h == -1:
            return -1

        right_h = self.node.right.checkHeight()
        if right_h == -1:
            return -1

        diff_h = left_h - right_h
        if diff_h > 1:
            return -1
        else:
            return max(left_h, right_h) + 1

    def isBalanced(self):
        if self.checkHeight() == -1:
            return False
        return True


if __name__ == "__main__":
    t = BinaryTree ( )

    t.insert ( 12 )
    t.insert ( 8 )
    t.insert ( 4 )
    t.insert ( 16 )
    t.insert ( 13 )
    t.insert ( 17 )
    t.insert(2)
    # t.insert(1)

    # calculate height and balance for each node to can check if it's balanced or not
    # t.updateHeight()
    # t.updateBalance()

    # print ( t.checkBalanced ( ) )
    print( t.isBalanced() )
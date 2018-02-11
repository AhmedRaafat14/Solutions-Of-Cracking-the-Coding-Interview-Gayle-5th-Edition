from Chapter_4.AVLNode import Node

class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0   # define balance factor h2 - h1

    # This to insert new node in tree without repetting and rebalancing tree
    def insert(self, data):
        new_node = Node(data)
        # If there's no nodes in tree
        if not self.node:
            self.node       = new_node
            self.node.left  = AVLTree()
            self.node.right = AVLTree()
        # if node less than current node value insert in left
        elif data < self.node.data:
            self.node.left.insert(data)
        # if node greater than current node value insert in right
        elif data > self.node.data:
            self.node.right.insert(data)

        # Else, it exist return from insertion method

        # rebalancing the tree if needed
        self.rebalance()

    # rebalancing the tree to follow AVL tree rules
    def rebalance(self):
        """
            After inserting or deleting a node it's better to check
            the tree balance if it need rebalance so it will rebalance
            itself
        :return: void
        """

        # First of all update all node heights and balance factor for each one
        self.updateHeight(False)
        self.updateBalance(False)

        '''
            For rotation we have 4 cases:
                I.     Left Rotation
                II.    Right Rotation
                III.   Left-Right Rotation
                IIII.  Right-Left Rotation
        '''
        while self.balance < -1 or self.balance > 1:
            # left subtree is larger than right subtree
            if self.balance > 1:
                # Left, Right case ---> rotate y, z to th left
                if self.node.left.balance < 0:
                    '''
                        We make our node to be root for it's parent
                        and it's parent be it's left child and make 
                        our node (z) left child to be rigt child for
                        node (y)
                         x               x
                        / \             / \
                       y   D           z   D
                      / \        ->   / \
                     A   z           y   C
                        / \         / \
                       B   C       A   B
                    '''
                    self.node.left.LRotation()
                    self.updateHeight()
                    self.updateBalance()
                # Left Left case, roatet z, x to the right
                '''
                           x                 z
                          / \              /   \
                         z   D            y     x
                        / \         ->   / \   / \
                       y   C            A   B C   D 
                      / \ 
                     A   B
                '''
                self.RRotation()
                self.updateHeight()
                self.updateBalance()

            # Right subtree is larger than left subtree
            if self.balance < -1:
                # Right Left case, rotate z, x to right
                if self.node.right.balance > 0:
                    #     y               y
                    #    / \             / \
                    #   A   x           A   z
                    #      / \    ->       / \
                    #     z   D           B   x
                    #    / \                 / \
                    #   B   C               C   D
                    self.node.right.RRotation()
                    self.updateHeight()
                    self.updateBalance()

                # Right Right case, z, y to left
                #       y                 z
                #      / \              /   \
                #     A   z            y     x
                #        / \     ->   / \   / \
                #       B   x        A   B C   D
                #          / \
                #         C   D
                self.LRotation()
                self.updateHeight()
                self.updateBalance()

        return

    def updateHeight(self, recursive = True):
        """
        Update tree height it the longest path from root to fairst
        leaf + 1
        :param recursive: boolean to applay recursive mode or not 
        :return: void
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.updateHeight()
                if self.node.right:
                    self.node.right.updateHeight()

            self.height = 1 + max( self.node.left.height, self.node.right.height )
        else:
            self.height = -1

    def updateBalance(self, recursive = True):
        """
        this to calculate the node balance factor by :
        factor = height(left sub tree) - height(right sub tree)
        :param recursive: 
        :return: void
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.updateBalance()
                if self.node.right:
                    self.node.right.updateBalance()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def RRotation(self):
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def LRotation(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, data):
        if self.node:
            if self.node.data == data:
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                elif not self.node.left.node:
                    self.node = self.node.right.node
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    # find sucessor ad the smallest node in right
                    # or predesscor as largest node in left
                    successor = self.node.right.node
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.data = successor.data

                        self.node.right.delete(successor.data)

            elif data < self.node.data:
                self.node.left.delete(data)
            elif data > self.node.data:
                self.node.right.delete(data)

            # finally rebalance tree to confirm it's still AVL tree
            self.rebalance()

    def checkBalanced(self):
        if not self or not self.node:
            return True

        self.updateHeight()
        self.updateBalance()

        return ( ( abs(self.balance) < 2 ) and self.node.left.checkBalanced() and self.node.right.checkBalanced() )

    def inOrder(self):
        if not self.node:
            return []

        nodes = []
        left = self.node.left.inOrder()
        for el in left:
            nodes.append(el)

        nodes.append(self.node.data)

        right = self.node.right.inOrder()
        for el in right:
            nodes.append(el)

        return nodes

    def preOrder(self):
        if not self.node:
            return []

        nodes = []
        nodes.append ( self.node.data )

        left = self.node.left.inOrder()
        for el in left:
            nodes.append(el)

        right = self.node.right.inOrder()
        for el in right:
            nodes.append(el)

        return nodes

    def traverse(self, node = None, level = 0):
        if not node:
            node = self.node

        if node.right.node:
            self.traverse(node.right.node, level + 1)
            # print( ('\t' * level), '   /')

        print( 'level: '+ str(level) + '->' + str(node.data) )

        if node.left.node:
            # print ( ('\t' * level) , '   \\' )
            self.traverse ( node.left.node , level + 1 )
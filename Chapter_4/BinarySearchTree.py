

class BinarySearchTree:
    def __init__(self, val):
        self.data = val
        self.left_child = None
        self.right_child = None

    # insert new node to right or left of current node
    def insert(self, data):
        if data <= self.data and self.left_child:
            self.left_child.insert(data)
        elif data <= self.data:
            self.left_child  =  BinarySearchTree(data)
        elif data > self.data and self.right_child:
            self.right_child.insert(data)
        else:
            self.right_child  =  BinarySearchTree(data)


    # check if this node value based in BST or not
    def find(self, data):
        if data < self.data and self.left_child:
            return self.left_child.find(data)
        if data > self.data and self.right_child:
            return self.right_child.find(data)

        return data == self.data

    # remove node from tree
    def remove(self, data, parent):
        if data < self.data and self.left_child:
            return self.left_child.remove(data, self)
        elif data < self.data:
            return False
        elif data > self.data and self.right_child:
            return self.right_child.remove(data, self)
        elif data > self.data:
            return False
        else:
            # #1: if node doesn't have any childs
            if not self.left_child and not self.right_child and self == parent.left_child:
                parent.left_child = None
                self.clear()
            elif not self.left_child and not self.right_child and self == parent.right_child:
                parent.right_child = None
                self.clear()

            # 2: if node has at least one child left or right
            elif self.left_child and not self.right_child and self == parent.right_child:
                parent.left_child = self.left_child
                self.clear()
            elif self.left_child and not self.right_child and self == parent.left_child:
                parent.right_child = self.left_child
                self.clear()
            elif not self.left_child and self.right_child and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear()
            elif not self.left_child and self.right_child and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear()
            else:
                self.data = self.right_child.find_min()
                self.right_child.remove(self.data, self)

            return True

    # clear node value
    def clear(self):
        self.value = self.left_child = self.right_child = None

    # find min value between two childs
    def find_min(self):
        if self.left_child:
            return self.left_child.find_min()
        return self.data

    def pre_order(self, nodes = []):
        if not nodes:
            nodes = []

        nodes.append( self.data )
        # print(self.data)

        if self.left_child:
            self.left_child.pre_order( nodes )

        if self.right_child:
            self.right_child.pre_order( nodes )
        return nodes

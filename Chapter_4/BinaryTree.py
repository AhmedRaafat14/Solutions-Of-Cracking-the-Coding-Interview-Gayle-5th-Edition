
from Chapter_3.Queue import Queue

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    # insert node to left of some node
    def insert_left(self, data):
        if not self.left_child:
            self.left_child = BinaryTree( data )
        else:
            new_node = BinaryTree( data )
            new_node.left_child, self.left_child = self.left_child, new_node

        return

    # insert node to the right of some node
    def insert_right(self, data):
        if not self.right_child:
            self.right_child = BinaryTree ( data )
        else:
            new_node = BinaryTree ( data )
            new_node.right_child , self.right_child = self.right_child , new_node

        return

    ''' Imlment DFS types: pre_order(), in_order() and post_order() '''
    def pre_order(self, nodes = []):
        # if not nodes:
        #     nodes = []

        # nodes.append( self.data )
        print(self.data)

        if self.left_child:
            self.left_child.pre_order( nodes )

        if self.right_child:
            self.right_child.pre_order( nodes )
        return nodes

    def in_order(self, nodes = []):
        # if not nodes:
        #     nodes = []

        if self.left_child:
            self.left_child.in_order( nodes )

        print ( self.data )
        # nodes.append( self.data )

        if self.right_child:
            self.right_child.in_order ( nodes )

        # return nodes

    def post_order(self, nodes = []):
        # if not nodes:
        #     nodes = []

        if self.left_child:
            self.left_child.post_order( nodes )

        if self.right_child:
            self.right_child.post_order ( nodes )

        print(self.data)
        # nodes.append( self.data )
        # return nodes

    ''' Implment BFS '''
    def BFS(self):
        nodes = []
        q = Queue()
        q.enqueue(self)
        while not q.isEmpty():
            current_node = q.dequeue()
            # print( current_node.data )
            nodes.append( current_node.data )

            if current_node.left_child:
                q.enqueue( current_node.left_child )

            if current_node.right_child:
                q.enqueue( current_node.right_child )

        return nodes

'''
Describe how you could use a single 
    array to implement three stacks.
'''

class ThreeStacks ( ):
    def __init__(self):
        self.array = [ None , None , None ]
        self.current = [ 0 , 1 , 2 ]

    def push(self , item , stack_number):
        if not stack_number in [ 0 , 1 , 2 ]:
            raise Exception ( "Bad stack number" )
        while len ( self.array ) <= self.current[ stack_number ]:
            self.array += [ None ] * len ( self.array )
        self.array[ self.current[ stack_number ] ] = item
        self.current[ stack_number ] += 3

    def pop(self , stack_number):
        if not stack_number in [ 0 , 1 , 2 ]:
            raise Exception ( "Bad stack number" )
        if self.current[ stack_number ] > 3:
            self.current[ stack_number ] -= 3
        item = self.array[ self.current[ stack_number ] ]
        self.array[ self.current[ stack_number ] ] = None


        return item

#       Test using LinkedList
from Chapter_3.Stack import LStack as Stack
from Chapter_3.Queue import LQueue as Queue

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

# print( *q.traverse(), sep='--->' )
# q.reverse()
# q.dequeue()
# print( q.size() )
# print( *q.traverse(), sep='--->' )


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print( s.size() )
#
# print( *s.traverse(), sep='--->' )
# print( s.search(10) )
# # s.pop()
# # s.reverse()
# print( s.peek() )
# print( *s.traverse(), sep='--->' )

#  Test using Lists
# from Chapter_3.Stack import Stack
# from Chapter_3.Queue import Queue

# s = Stack()
#
# # print( s.isEmpty() )
# s.push( 4 )
# s.push( 'dog' )
# # print( s.peek() )
# s.push( True )
# # print( s.size() )
# # print( s.isEmpty() )
# s.push( 8.4 )
# print( s.pop() )
# print( s.pop() )
# print( s.size() )
#
# print( *s.traverse () ,  sep = '-->' )
# print( *s.reverse  ()  , sep = '-->' )
#
# q = Queue()
#
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
#
# print( *q.traverse(), sep='<--' )
# q.dequeue()
# print( *q.traverse(), sep='<--' )
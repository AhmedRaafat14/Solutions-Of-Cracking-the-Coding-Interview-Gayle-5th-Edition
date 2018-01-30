
from Chapter_2.SingleLinkedList import UnorderedList as UnList

'''
Write code to remove duplicates from an unsorted linked list.
'''
def p_2_1():
    """
    Write code to remove duplicates from an unsorted linked list.
    :return: void 
    """
    myList = UnList()
    myList.append ( 1 )
    myList.append ( 3 )
    myList.append ( 2 )
    myList.append ( 1 )
    myList.append ( 4 )
    myList.append ( 2 )
    myList.append ( 3 )

    print('Before:')
    print ( *myList.traverse ( ) , sep='--->' )

    myList.removeDuplicates()

    print("After:")
    print(*myList.traverse(), sep='--->')


'''
Implement an algorithm to find the kth to last element of
 a singly linked list.
'''
def p_2_2():
    myList = UnList ( )
    myList.append ( 1 )
    myList.append ( 3 )
    myList.append ( 2 )
    myList.append ( 1 )
    myList.append ( 4 )
    myList.append ( 2 )
    myList.append ( 3 )

    k = 8
    # get the size of list
    list_len = myList.size()
    nodes = []
    for i in range(k, list_len + 1):
        el = myList.findByPos(i)
        if el < 0:
            break
        nodes.append(str(el))

    print( *nodes, sep='--->' ) if nodes else print('No elemnts')

'''
Implement an algorithm to delete a node in the middle 
of a singly linked list, given only access to that node.
'''
def p_2_3():
    myList = UnList ( )
    myList.append ( 1 )
    myList.append ( 2 )
    myList.append ( 3 )
    myList.append ( 4 )
    myList.append ( 5 )
    myList.append ( 6 )
    myList.append ( 7 )

    # delete by position
    deleted_node_pos = 3

    # delete by node value
    deleted_node = 8

    print ( 'Before:' )
    print ( *myList.traverse ( ) , sep='--->' )

    # myList.popByPos ( deleted_node_pos )
    myList.remove(deleted_node)

    print ( "After:" )
    print ( *myList.traverse ( ) , sep='--->' )

'''
Write code to partition a linked list around a value x, 
such that all nodes less than x come before all nodes 
greater than or equal to x.
'''
def p_2_4():
    myList = UnList()
    myList.append ( 4 )
    myList.append ( 5 )
    myList.append ( 2 )
    myList.append ( 1 )
    myList.append ( 3 )
    myList.append ( 6 )

    X = 3

    print ( 'Before:' )
    print ( *myList.traverse ( ) , sep='--->' )

    myList.partition(X)
    # myList.sort()

    print ( "After:" )
    print ( *myList.traverse ( ) , sep='--->' )


if __name__ == "__main__":
    # p_2_1()
    # p_2_2()
    # p_2_3()
    p_2_4()
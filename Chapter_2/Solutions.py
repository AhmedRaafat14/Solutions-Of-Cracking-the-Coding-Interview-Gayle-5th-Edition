
from Chapter_2.SingleLinkedList import UnorderedList as UnList
from Chapter_2.Node import Node

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

'''
You have two numbers represented by a linked list, 
where each node contains a single digit. The digits are stored 
in reverse order, such that the Ts digit is at the head of the list.
Write a function that adds the two numbers and returns the sum 
    as a linked list.
EXAMPLE:
    Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
    Output: 2 -> 1 -> 9.That is, 912.
'''
def p_2_5_v1():  # in reversed order
    num1 = UnList()
    # use push function to put digit in the first of list.
    num1.push(6)
    num1.push(1)
    num1.push(7)

    # print('number 1:')
    print(*num1.traverse(), sep='--->')

    num2 = UnList ( )
    # use push function to put digit in the first of list.
    num2.push ( 2 )
    num2.push ( 9 )
    num2.push ( 5 )

    res = sum_lists(num1, num2)
    li = []
    while res:
        li.append(str(res.getData()))
        res = res.getNext()

    print(*li, sep='--->')

    # print ( 'number 2:' )
    print ( *num2.traverse ( ) , sep='--->' )

    # now we have two nubers in reversed order so firs of all get each number
    # digits in one integer number if we just leav as it traversed will be
    # in wrong order like for 617 will be 716 so to reverse it use reversed
    # function implmented in linked list class
    # num1.reverse()
    # num2.reverse()
    # number1 = int( "".join(map(str, num1.traverse())) )
    # number2 = int( "".join(map(str, num2.traverse())) )
    #
    # print("=====================================")
    #
    # print(number1, number2)
    #
    # s_n_1_2 = number1 + number2
    # print("number1 + number 2 = " + str(s_n_1_2))
    #
    # # now store it in linked list reversed to be 912 ==> 219
    # result = UnList()
    # for digit in str(s_n_1_2):
    #     result.push(digit)
    #
    # print("Result:")
    # print(*result.traverse(), sep="--->")

    return

def p_2_5_v2():  # in normal order
    num1 = UnList()
    # use push function to put digit in the first of list.
    num1.append(6)
    num1.append(1)
    num1.append(7)

    # print('number 1:')
    print(*num1.traverse(), sep='--->')

    num2 = UnList ( )
    # use push function to put digit in the first of list.
    num2.append ( 2 )
    num2.append ( 9 )
    num2.append ( 5 )

    # print ( 'number 2:' )
    print ( *num2.traverse ( ) , sep='--->' )

    # now we have two nubers in reversed order so firs of all get each number
    # digits in one integer number
    number1 = int( "".join(map(str, num1.traverse())) )
    number2 = int( "".join(map(str, num2.traverse())) )

    # print("=====================================")
    #
    # print(number1, number2)
    #
    s_n_1_2 = number1 + number2
    # print("number1 + number 2 = " + str(s_n_1_2))
    #
    # now store it in linked list
    result = UnList()
    for digit in str(s_n_1_2):
        result.append(digit)

    print("Result:")
    print(*result.traverse(), sep="--->")

def sum_lists(num1, num2):
    node1, node2 = num1.head, num2.head
    carry = 0
    result_head, result_node = None, None
    while node1 or node2 or carry:
        value = carry
        if node1:
          value += node1.getData()
          node1 = node1.getNext()
        if node2:
          value += node2.getData()
          node2 = node2.getNext()
        if result_node:
          result_node.setNext( Node(value % 10) )
          result_node = result_node.getNext()
        else:
          result_node = Node(value % 10)
          result_head = result_node
        carry = value // 10
    return result_head

'''
Given a circular linked list, implement an algorithm which 
returns the node at the beginning of the loop.
DEFINITION
    Circular linked list: A (corrupt) linked list in which a node's 
            next pointer points to an earlier node, 
            so as to make a loop in the linked list.
EXAMPLE:
    Input: A - > B - > C - > D - > E - > C [the same C as earlier]
    Output: C
'''
def p_2_6():
    circ = UnList()
    circ.append ( 'A' )
    circ.append ( 'B' )
    circ.append ( 'C' )
    circ.append ( 'D' )
    circ.append ( 'E' )
    circ.append ( 'C' )

    print( circ.findStartOfLoop() )
    return

'''
Implement a function to check if a linked list is a palindrome
'''
def p_2_7():
    myList = UnList ( )
    myList.append ( 1 )
    myList.append ( 2 )
    myList.append ( 3 )
    myList.append ( 4 )
    myList.append ( 3 )
    myList.append ( 2 )
    myList.append ( 1 )

    # myListRevesed = myList
    #
    # myListRevesed.reverse()
    #
    # l1 = myList.traverse()
    # l2 = myListRevesed.traverse()
    #
    # error = False
    # for i in range( (len(l1) // 2) + 1 ):
    #     if l1[i] != l2[i]:
    #         error = True
    #         break
    #
    # print(not error)
    print(myList.isPalindrome())

    # print ( *myList.traverse ( ) , sep='--->' )
    # print ( *myListRevesed.traverse ( ) , sep='--->' )


if __name__ == "__main__":
    # p_2_1()
    # p_2_2()
    # p_2_3()
    # p_2_4()
    # p_2_5_v1()
    # p_2_5_v2()
    # p_2_6()
    p_2_7()

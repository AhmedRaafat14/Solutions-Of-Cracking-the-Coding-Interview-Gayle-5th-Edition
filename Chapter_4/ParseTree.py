
from Chapter_3.Stack import Stack
from Chapter_4.BinaryTree import BinaryTree

def buildParseTree(exp):
    exp_lis = exp.split()
    p_st = Stack()
    exp_tree = BinaryTree('')
    p_st.push(exp_tree)
    current = exp_tree
    for ch in exp_lis:
        # if current token is '(', add new node as left child for current
        # and omve to left child
        if ch == '(':
            current.insert_left('')
            p_st.push(current)
            current = current.left_child
        # if current token not in the list ['+', '-', '*', '/', ')']
        # so it's number set the current node value to
        # current token integer value
        elif ch not in ['+', '-', '*', '/', ')']:
            current.data = int(ch)
            current = p_st.pop()
            # current = parent
        # if current token in the list ['+', '-', '*', '/']
        # assign current node data to curent token and insert new node
        # to right child, then go to right child
        elif ch in ['+', '-', '*', '/']:
            current.data = ch
            current.insert_right('')
            p_st.push(current)
            current = current.right_child
        # if current token is ')' so go to the parent of current node
        elif ch == ')':
            current = p_st.pop()
        else:
            raise ValueError

    return exp_tree




pt = buildParseTree("( ( 10 + 5 ) * 3 )")
# pt.post_order()
print( pt.post_oper_order() )
print(pt.printexp())
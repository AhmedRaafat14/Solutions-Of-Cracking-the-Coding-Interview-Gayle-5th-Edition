from Chapter_4.BinaryTree import BinaryTree
# from Chapter_4.BinarySearchTree import BinarySearchTree
#
# bst = BinarySearchTree(50)
#
# bst.insert(21)
# bst.insert(76)
# bst.insert(4)
# bst.insert(32)
# bst.insert(64)
# bst.insert(52)
# bst.insert(100)
#
# # bst.pre_order()
# print(bst.pre_order())
# bst.remove(76, None)
# print(bst.pre_order())
# print( bst.find(100) )


a_n = BinaryTree(1)
a_n.insert_left(2)
a_n.insert_right(5)

b_n = a_n.left_child
b_n.insert_right(4)
b_n.insert_left(3)

c_n = a_n.right_child
c_n.insert_left(6)
c_n.insert_right(7)

print( *a_n.dfs(), sep='----' )
print( *a_n.pre_order(), sep='----' )
#
# d_n = b_n.right_child
# e_n = c_n.left_child
# f_n = c_n.right_child
#
# n_pre = n_in = n_post = []
#
# print( *a_n.BFS(), sep=' ---- ' )

# print('pre-order')
# a_n.pre_order()
# print('in-order')
# a_n.in_order()
# print('post-order')
# a_n.post_order()

# print( *a_n.pre_order(), sep='---' )
print( *a_n.in_order(), sep='----' )
print( *a_n.post_order(), sep='----' )




# print(a_n.data)
# print(b_n.data)
# print(c_n.data)
# print(d_n.data)
# print(e_n.data)
# print(f_n.data)
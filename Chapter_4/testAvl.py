from Chapter_4.AVLTree import AVLTree



avl = AVLTree()

data = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 ]

for key in data:
    avl.insert ( key )
#
# for key in [ 4 , 3 ]:
#     avl.delete ( key )

# print(  avl.inOrder() )
# print(  avl.preOrder() )
# print(  avl.checkBalanced() )

avl.traverse()
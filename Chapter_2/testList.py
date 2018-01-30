import Node
import SingleLinkedList as SingleList
import DoubleLinkedList as DoubleList


print("=======>  Double Linked List  <==========")

dlist = DoubleList.DoubleLinkedList()

# print(dlist.isEmpty())

dlist.push(22)
dlist.push(45)

# print(dlist.isExist(22))
# print(dlist.isExist(23))

dlist.append(23)

# print(dlist.index(22))

# print(dlist.findByPos(3))

# print(dlist.findAfterPos(4))
# print(dlist.remove(23))
# print(dlist.pop())
# print(dlist.popByPos(1))
# print(dlist.insertBefore(3, 20))
print(dlist.insertAfter(2, 20))

print(*dlist.traverse(), sep='<-->')


print("=======>  End of Double Linked List  <==========")

# print("=========>        Ordered List    <=============")
# myOlist = SingleList.OrderedList()
# # print('fkdfkd')
# myOlist.add(31)
# myOlist.add(77)
# myOlist.add(17)
# myOlist.add(93)
# myOlist.add(26)
# myOlist.add(54)
#
# print(myOlist.size())
# print(myOlist.search(93))
# print(myOlist.search(100))
#
# myOlist.add(27)
# myOlist.remove(31)
#
# print('index of 93 is: ' + str(myOlist.index(93)))
# print('item in pos 4 is: ' + str(myOlist.findByPos(4)))
#
# print(myOlist.pop())
# print(myOlist.popByPos(1))
#
# print(*myOlist.traverse(), sep='->')
#
# myOlist.reverse()
# print(*myOlist.traverse(), sep='->')
#
# print("=========>       End of Ordered List    <=============")
#
#
# print("=========>        Unordered List    <=============")
#
# mylist = SingleList.UnorderedList()
#
# mylist.push(31)
# mylist.push(77)
# mylist.push(17)
# mylist.push(93)
# mylist.push(26)
# mylist.push(54)
#
# print(mylist.size())
# print(mylist.search(93))
# print(mylist.index(93))
# print(mylist.search(100))
#
# mylist.push(100)
# print(mylist.search(100))
# print(mylist.index(100))
# print(mylist.size())
#
# mylist.remove(54)
# print(mylist.size())
# mylist.remove(93)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())
# print(mylist.search(93))
#
# mylist.append('ahmad')
#
#
# print('Value of node at pos: 3 is : ' + str(mylist.findByPos(3)) )
#
# print('Traverse all nodes:  ')
# print(*mylist.traverse(), sep='->')
#
# print(mylist.pop())
# print(mylist.popByPos(1))
#
# print(*mylist.traverse(), sep='->')
#
# mylist.reverse()
# print(*mylist.traverse(), sep='->')
# print("=========>        End of Unordered List    <=============")
'''
In the classic problem of the Towers of Hanoi, 
you have 3 towers and N disks of different sizes which can 
slide onto any tower. The puzzle starts with disks sorted
in ascending order of size from top to bottom 
(i.e., each disk sits on top of an
even larger one). 
You have the following constraints:
    (1) Only one disk can be moved at a time.
    (2) A disk is slid off the top of one tower onto 
            the next tower.
    (3) A disk can only be placed on top of a larger disk.

Write a program to move the disks from the first tower to the 
last using stacks.
'''

class Stack:
    # Initalize the "items" stack
    def __init__(self):
        self.items = []

    # add a new element to the top of the stack
    def push(self, item):
        self.items.append(item)

    # remove an element from the top of the stack
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return "Stack Empty"

    # traverse stack list
    def traverse(self):
        return self.items


class TowerOfHanoi:
    def __init__(self, num_disks):
        self.numDisks = num_disks
        self.towers = [Stack(), Stack(), Stack()]
        for i in range(num_disks, -1, -1):
            self.towers[0].push(i)

    def traverse(self):
        tows = []
        for i in range(len(self.towers)):
            tows.append( self.towers[i].traverse() )

        return tows

    def moveDisks(self, source, dest):
        self.towers[dest].push( self.towers[source].pop() )

    def moveTower(self, n, source, spare, dest):
        if n == 0:
            self.moveDisks(source, dest)
        else:
            self.moveTower(n - 1, source, dest, spare)
            self.moveDisks(source, dest)
            self.moveTower(n - 1, spare, source, dest)


t = TowerOfHanoi(5)

print( t.traverse() )

t.moveTower(5, 0, 1, 2)

print( t.traverse() )
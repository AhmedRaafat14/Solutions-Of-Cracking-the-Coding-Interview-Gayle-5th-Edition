'''

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

'''
    Best tutorail for that :
http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html

the left child of a parent (at position p) is the node 
that is found in position 2p in the list. 
Similarly, the right child of the parent is at position 2p+1 
in the list.

The heap order property is as follows: In a heap, for every 
node x with parent p, the key in p is smaller than or 
equal to the key in x.
'''

class BinaryHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.perlocateUp( self.size )

    def perlocateUp(self, idx):
        while idx//2 > 0:
            if self.heap[idx] < self.heap[idx//2]:
                self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]

            idx //= 2

    def perlocateDown(self, idx):
        while (idx * 2) <= self.size:
            min_child = self.minChildIdx(idx)
            if self.heap[idx] > self.heap[min_child]:
                self.heap[idx], self.heap[min_child] = self.heap[min_child], self.heap[idx]

            idx = min_child

    def minChildIdx(self, idx):
        if idx * 2 + 1 > self.size or self.heap[idx*2] < self.heap[idx*2+1]:
            return idx * 2
        else:
            return idx * 2 + 1

    def delMinChild(self):
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.perlocateDown(1)
        return removed

    def buildHeap(self, lis):
        self.heap = [0] + lis
        self.size = len(lis)
        i = self.size//2
        while i > 0:
            self.perlocateDown(i)
            i -= 1


bh = BinaryHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMinChild())
print(bh.delMinChild())
print(bh.delMinChild())
print(bh.delMinChild())
print(bh.delMinChild())
'''
An animal shelter holds only dogs and cats, and operates 
on a strictly "first in, first out" basis. People must adopt 
either the "oldest" (based on arrival time) of all animals 
at the shelter, or they can select whether they would prefer 
a dog or a cat (and will receive the oldest animal of that type). They cannot select which
specificanimal they would like. Create the data structures 
to maintain this system and implement operations such as 
enqueue, dequeueAny, dequeueDog and dequeueCat.
You may use the built-in LinkedList data structure.
'''
import time


class Animal:
    def __init__(self, name):
        self.name = name
        self.order = int(round(time.time() * 1000))

    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

class Queue:
    # Initalize the "items" Queue
    def __init__(self):
        self.cats, self.dogs = [], []

    def isEmpty(self):
        return self.cats == [] and self.dogs == []

    def enqueue(self, name, type):
        if type == 'cat':
            new_animal = Animal(name)
            self.cats.append(new_animal)
        elif type == 'dog':
            new_animal = Animal ( name )
            self.dogs.append(new_animal)

    def dequeueCat(self):
        if len(self.cats) > 0:
            tmp = self.cats[0]
            self.cats = self.cats[1:]
            return tmp.getName()
        return "Cats Queue Empty"

    def dequeueDog(self):
        if len(self.dogs) > 0:
            tmp = self.dogs[0]
            self.dogs = self.dogs[1:]
            return tmp.getName()
        return "Dogs Queue Empty"

    def dequeueAny(self):
        if len(self.cats) == 0:
            tmp = self.dogs[ 0 ]
            self.dogs = self.dogs[1:]
            return tmp.getName()
        elif len(self.dogs) == 0:
            tmp = self.cats[0]
            self.cats = self.cats[1:]
            return tmp.getName()

        tmp_cat = self.cats[0]
        tmp_dog = self.dogs[0]
        print(tmp_cat.getOrder(), tmp_dog.getOrder())

        if tmp_cat.getOrder() <= tmp_dog.getOrder():
            self.cats = self.cats[ 1: ]
            return tmp_cat.getName()
        else:
            self.dogs = self.dogs[1:]
            return tmp_dog.getName()

q = Queue()

q.enqueue('c1', 'cat')
q.enqueue('d1', 'dog')
q.enqueue('c2', 'cat')
q.enqueue('d2', 'dog')
q.enqueue('c3', 'cat')
q.enqueue('d3', 'dog')
q.enqueue('c4', 'cat')
q.enqueue('d4', 'dog')

print( q.dequeueCat() )
print( q.dequeueDog() )
print( q.dequeueAny() )
print( q.dequeueAny() )
# print( q.dequeueAny() )
# print( q.dequeueAny() )
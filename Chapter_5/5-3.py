"""
Given a positive integer, print the next smallest and the next 
largest number that have the same number of 1 bits in their 
binary representation.
"""

def getNext(n):
    tmp = n
    c0, c1 = 0, 0

    # count number of zeros
    while (tmp & 1) == 0 and tmp != 0:
        c0 += 1
        tmp >>= 1

    # count number of ones
    while tmp & 1 == 1:
        c1 += 1
        tmp >>= 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return None


    p = c0 + c1

    n = n | (1 << p)
    n = n & ~( (1 << p) - 1 )
    n = n | (1 << (c1 - 1)) - 1

    return n

def getPrev(n):
    tmp = n
    c0, c1 = 0, 0

    while tmp & 1 == 1:
        c1 += 1
        tmp >>= 1

    if tmp == 0:
        return None

    while (tmp & 1) == 0 and tmp != 0:
        c0 += 1
        tmp >>= 1

    p = c0 + c1

    n = n & ( (~0) << (p + 1) )
    mask = (1 << (c1 + 1)) - 1
    n = n | (mask << (c0 - 1))

    return n

def getNextArthmetic(n):
    tmp = n
    c0 , c1 = 0 , 0

    # count number of zeros
    while (tmp & 1) == 0 and tmp != 0:
        c0 += 1
        tmp >>= 1

    # count number of ones
    while tmp & 1 == 1:
        c1 += 1
        tmp >>= 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return None

    return n + (1 << c0) + (1 << (c1 - 1)) - 1

def getPrevArthmetic(n):
    tmp = n
    c0 , c1 = 0 , 0

    while tmp & 1 == 1:
        c1 += 1
        tmp >>= 1

    if tmp == 0:
        return None

    while (tmp & 1) == 0 and tmp != 0:
        c0 += 1
        tmp >>= 1

    return n - (1 << c1) - (1 << (c0 - 1)) + 1

def getNumbs(n):
    return getPrev(n), getNext(n)

def getNumbsArthmetic(n):
    return getPrevArthmetic(n), getNextArthmetic(n)

if __name__ == "__main__":
    print ( getNumbs ( 8  ) )
    print ( getNumbs ( 12 ) )
    print ( getNumbs ( 15 ) )

    print ( getNumbsArthmetic ( 8 ) )
    print ( getNumbsArthmetic ( 12 ) )
    print ( getNumbsArthmetic ( 15 ) )
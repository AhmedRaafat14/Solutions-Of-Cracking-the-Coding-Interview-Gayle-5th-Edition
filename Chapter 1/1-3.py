'''
Given two strings, write a method to decide if one is a permutation of the other.
'''

def is_permute(S1, S2):
    counter = {}

    for ch in S1:
        if ch not in counter:
            counter[ch] = 1
            continue
        counter[ch] += 1

    for ch in S2:
        if ch not in counter:
            return  False
        counter[ch] -= 1
        if counter[ch] == 0:
            del counter[ch]

    if len(counter) == 0:
        return True

def is_permute_simple(S1, S2):
    return True if sorted(S1) == sorted(S2) else False

def is_permute_simple_counter(S1, S2):
    for i in range(len(S1)):
        if S1.count(S1[i]) != S2.count(S1[i]):
            return False

    return True


if __name__ == "__main__":
    print( is_permute('ahmed', 'ahmed') )
    print( is_permute_simple_counter('ahmed', 'ahmed') )
    print( is_permute('ahmed', 'ahmad') )
    print( is_permute_simple('ahmed', 'ahmad') )

'''
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, si and s2, write code to check if s2 is
a rotation of si using only one call to isSubstring (e.g.,"waterbottle"is a rota-
tion of "erbottlewat")
'''


def is_rotation(s1, s2):
    if len(s1) == len(s2):
        return False

    return is_substring(s1 + s1, s2)


def is_substring(s1, s2):
    # Fastest solution
    # return s2 in s1

    if len(s2) > len(s1):
        return False

    for i in range(len(s1) - len(s2) - 1):
        is_sub = 0
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                is_sub = 1
                break

    if is_sub:
        return True
    return False


if __name__ == "__main__":
    print(is_rotation('waterbottle', 'erbottlewa'))

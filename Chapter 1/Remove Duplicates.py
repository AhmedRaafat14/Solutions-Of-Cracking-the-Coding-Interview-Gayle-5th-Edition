"""
Design an algorithm and write code to remove the duplicate
characters in a string without using any additional buffer
NOTE: One or two additional variables are fine An extra copy of the array is not.

Test Cases:
1. String is null
2. String is just one char
3. String having all duplicates
4. String having no duplicates
5. String having continues duplicates
6. String having non-continues duplicates
"""


def remove_dup(s):
    if s == "":
        return s
    n = len(s)
    if n < 2:
        return s

    i = 0
    while i < n:
        if s[i] in s[:i]:
            del s[i]
            n -= 1
        else:
            i += 1
    return s


if __name__ == "__main__":
    print(remove_dup(""))

    print(remove_dup("a"))

    print("".join(remove_dup(list("as"))))

    print("".join(remove_dup(list("aaasss"))))

    print("".join(remove_dup(list("asasas"))))

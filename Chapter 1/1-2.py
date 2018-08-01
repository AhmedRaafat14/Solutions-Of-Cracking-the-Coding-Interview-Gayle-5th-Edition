"""
Implement a function void reverse(char* str) in C or C++ which reverses a null-
terminated string
"""


# Using python benefits =xD
def reverse_s(s):
    return s[::-1]


# Using Naive solution
def reverse_s_naive(s):
    new_s = ""
    for ch in s:
        new_s = ch + new_s
    return new_s


if __name__ == "__main__":
    print(reverse_s("test"))
    print(reverse_s("car"))
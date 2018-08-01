"""
Write a method to replace all spaces in a string with'%20'.

EXAMPLE
Input:  "Mr John Smith "
Output: "Mr%20John%20Smith"
"""


# Approach 1 using String manipulation methods
def replace_space(s):
    return (s.rstrip()).replace(" ", '%20')


# Approach 2 without using String manipulation methods
def replace_spaces(s):
    s_li = list(s)
    delm = ''

    for i in range(len(s) -1, -1, -1):
        if s_li[i].isalpha() and delm == '':
            delm = '%20'

        if s_li[i] == " ":
            s_li[i] = delm

    return "".join(s_li)


if __name__ == "__main__":
    print(replace_space("Mr John Smith"))

    print(replace_spaces("Mr John Smith"))
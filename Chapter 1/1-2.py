'''
Implement a function void reverse(char* str) in C or C++ which reverses a null-
terminated string
'''

s = input()

# First approach
# rev_s = ""
# for i in range(len(s) - 1, -1, -1):
#     rev_s += s[i]
#
# print(rev_s)

# Second approach
print(s[::-1])

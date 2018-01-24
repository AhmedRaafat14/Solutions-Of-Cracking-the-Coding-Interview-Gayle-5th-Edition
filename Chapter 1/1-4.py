'''
Write a method to replace all spaces in a string with'%20'. You may assume that
the string has sufficient space at the end of the string to hold the additional
characters, and that you are given the "true" length of the string. (Note: if imple-
menting in Java, please use a character array so that you can perform this opera-
tion in place.)
EXAMPLE
Input:
"Mr John Smith
Output: "Mr%20Dohn%20Smith"
'''

S = input()

# Approach 1 using String manipulation methods
# S = S.rstrip()
# print( S.replace(' ', '%20') )

# Approach 2 without using String manipulation methods
S_li = [ch for ch in S]
delm = ''

for i in range(len(S) - 1, -1, -1):
    if S_li[i].isalpha() and delm == '':
        delm = '%20'
    if S_li[i] == ' ':
        S_li[i] = delm

print( "".join(S_li) )

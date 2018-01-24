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
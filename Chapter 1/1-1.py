'''
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
'''

s = input()

flag = True

# First approch with Hash Map DS
# uniq_chs = {}
# for ch in s:
#     if ch in uniq_chs:
#         flag = False
#         break
#     else:
#         uniq_chs[ch] = 1

# Second approch without any DS
for ch in s:
    if s.count(ch) > 1:
        flag = False
        break

print('yes' if flag else 'no')

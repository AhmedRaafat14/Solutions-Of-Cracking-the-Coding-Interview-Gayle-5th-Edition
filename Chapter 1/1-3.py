s1 = input()
s2 = input()

# Approache 1
# print('yes' if sorted(s1) == sorted(s2) else 'no')

# Approache 2
flag = 1
for i in range(len(s1)):
    if s1.count(s1[i]) != s2.count(s1[i]):
        flag = 0
        break


print('yes' if flag else 'no')
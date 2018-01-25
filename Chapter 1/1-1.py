'''
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
'''

# First approch with Hash Map DS
def check_unique_chars_using_map(S):
    uniq_chs = {}
    flag = True
    for ch in S:
        if ch in uniq_chs:
            flag = False
            break
        else:
            uniq_chs[ch] = 1

    return True if flag else False

# Second approch without any DS
def check_unique_chars_without_map(S):
    flag = True
    for ch in S:
        if S.count ( ch ) > 1:
            flag = False
            break

    return True if flag else False

if __name__ == "__main__":
    print( check_unique_chars_using_map("ahmed") )
    print( check_unique_chars_without_map("ahmad") )

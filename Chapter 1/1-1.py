"""
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""


# First approach with Hash Map DS
def check_unique_chars_using_map(s):
    uniq_chs = {}

    for ch in s:
        if ch in uniq_chs:
            return False

        uniq_chs[ch] = 1

    return True


# Second approach without any DS
def check_unique_chars_without_map(s):
    for ch in s:
        if s.count(ch) > 1:
            return False
    return True


# Another approaches
def check_unique_using_list_set(s):
    if list(set(s)) == list(s):
        return True
    return False


if __name__ == "__main__":
    print(check_unique_chars_using_map("ahmed"))
    print(check_unique_chars_using_map("aaahmed"))

    print(check_unique_chars_without_map("ahmed"))
    print(check_unique_chars_without_map("ahmmad"))

    print(check_unique_using_list_set("ahmed"))
    print(check_unique_using_list_set("aaahmed"))
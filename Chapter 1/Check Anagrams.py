"""
Write a method to decide if two strings are anagrams or not
"""


# First approach using Python point of view "sorted()"
def check_anag(s1, s2):
    return True if sorted(s1) == sorted(s2) else False


# Second approach using loops and in keyword
def check_anagrams(s1, s2):
    for ch in s1:
        if ch not in s2:
            return False
    return True


if __name__ == "__main__":
    print(check_anag("abc", "cbd"))

    print(check_anagrams("test", "stet"))

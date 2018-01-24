'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the orig-
inal string, your method should return the original string
'''

s = input()

comp_s = ''
i = 0
while i < len(s):
    current_ch = s[i]
    j, ch_cnt = i + 1, 1
    while j < len(s) and s[j] == current_ch:
        ch_cnt += 1
        j += 1

    comp_s += current_ch + str(ch_cnt)
    i += ch_cnt

print( s if len(s) == len(comp_s) else comp_s )

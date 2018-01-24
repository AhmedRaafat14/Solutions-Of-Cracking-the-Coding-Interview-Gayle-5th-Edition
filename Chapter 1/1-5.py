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
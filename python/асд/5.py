def bad_character_table(pattern):
    table = {}
    m = len(pattern)
    for i in range(m):
        table[pattern[i]] = i
    return table

def good_suffix_table(pattern):
    m = len(pattern)
    table = [0] * (m + 1)
    suffix = [0] * (m + 1)
    for i in range(m):
        suffix[i] = m
    j = 0
    for i in range(m - 1, -1, -1):
        if pattern[i] == pattern[j]:
            j += 1
            suffix[i] = j
        else:
            j = 0

    for i in range(m):
        table[i] = m - suffix[0]
    for i in range(m):
        j = m - suffix[i]
        if table[j] > i - suffix[i] + 1:
            table[j] = i - suffix[i] + 1
    return table

def boyer_moore_matcher(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = bad_character_table(pattern)
    good_suffix = good_suffix_table(pattern)
    occurrences = []
    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            occurrences.append(shift)
            shift += good_suffix[0]
        else:
            bc_shift = j - bad_char.get(text[shift + j], -1)
            gs_shift = good_suffix[j + 1]
            shift += max(bc_shift, gs_shift)
    return occurrences

text = "ababcababac"
pattern = "ababa"
occurrences = boyer_moore_matcher(text, pattern)
print(f"Образец найден на позициях: {occurrences}")
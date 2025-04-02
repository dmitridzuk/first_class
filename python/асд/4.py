# Кнут
def compute_prefix_function(pattern):
    m = len(pattern)
    prefix_function = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix_function[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        prefix_function[i] = k
    return prefix_function

def kmp_matcher(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_function = compute_prefix_function(pattern)
    k = 0
    occurrences = []
    for i in range(n):
        while k > 0 and pattern[k] != text[i]:
            k = prefix_function[k - 1]
        if pattern[k] == text[i]:
            k += 1
        if k == m:
            occurrences.append(i - m + 1)
            k = prefix_function[k - 1]
    return occurrences

text = "abab  cab  abac"
pattern = "ab"
occurrences = kmp_matcher(text, pattern)
print(f"Образец найден на позициях: {occurrences}")
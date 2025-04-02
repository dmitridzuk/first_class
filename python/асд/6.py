def rabin_karp_matcher(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1, q)
    p_hash = 0
    t_hash = 0
    occurrences = []
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if pattern == text[i:i + m]:
                occurrences.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q
    return occurrences

text = "ababcababac"
pattern = "ababa"
occurrences = rabin_karp_matcher(text, pattern)
print(f"Образец найден на позициях: {occurrences}")
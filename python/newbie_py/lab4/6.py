def count_words(a):
    s = a.split()
    m = {}
    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    new_a = sorted(m.items(), key=lambda x: (-x[1], x[0]))
    return new_a

a = input("Введите текст(строку): ")
new_a= count_words(a)
for i, c in new_a:
    print(i)


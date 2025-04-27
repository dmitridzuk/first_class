def check(a):
    s = a.split()
    l = {}
    m = []
    for i in s:
        if i in l:
            l[i] += 1
        else:
            l[i] = 0
        m.append(l[i])
    return m

a = input("Введите строку: ")
c = check(a)
print(" ".join(str(i) for i in c))
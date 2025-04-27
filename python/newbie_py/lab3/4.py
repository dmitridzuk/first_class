def count_string(a):
    s = {}
    for i in a:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    return s

a = input("Введите список строк ЧЕРЕЗ ЗАПЯТУЮ СЛИТНО(пример: ффф,ааа,ччч): ").split(',')
s = count_string(a)
for i, c in s.items():
    print(c, end=' ')


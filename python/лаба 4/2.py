def chtoto(s1, s2):
    return s1.issubset(s2)
s1 = set(input("Введите элементы первого множества через запятую: ").split(","))
s2 = set(input("Введите элементы второго множества через запятую: ").split(","))
a = chtoto(s1, s2)
print(a)
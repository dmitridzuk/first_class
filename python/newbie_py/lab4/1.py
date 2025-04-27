def unique(a):
    new_a = set(a)
    return len(new_a)
a = input("Введите список чисел ЧЕРЕЗ ЗАПЯТУЮ СЛИТНО: ").split(",")
c = unique(a)
print("Количество различных чисел:", c)

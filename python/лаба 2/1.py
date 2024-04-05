#Треугольник Паскаля
def f(n):
    mas = [[1]]
    for i in range(1, n):
        m = [1]
        for j in range(1, i):
            m.append(mas[i - 1][j - 1] + mas[i - 1][j])
        m.append(1)
        mas.append(m)

    # Вывод треугольника
    width = len(" ".join(map(str, mas[-1])))
    for m in mas:
        print(" ".join(map(str, m)).center(width))

a = int(input("Введите количество строк: "))
f(a)
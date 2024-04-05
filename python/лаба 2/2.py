#Серпинский треугольник
import functools

def f(n):
    def h(m, i):
        x = " " * (2 ** i)
        return [f"{x}{d}{x}" for d in m] + [f"{d} {d}" for d in m]
    return functools.reduce(h, [i for i in range(n)], ["*"])

a = int(input("Введите число иттераций: "))
for i in f(a):
    print(i)
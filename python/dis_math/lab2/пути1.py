from math import comb

# Размер сетки
n = 16
m = 16

# Количество путей
paths = comb(n + m, n)

print(f"Количество кратчайших путей в сетке {n}x{m}: {paths}")
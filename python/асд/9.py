# полный перебор,
# метод ветвей и границ?
from itertools import permutations

def tsp(matrix):
    n = len(matrix)
    min_path = None
    min_cost = float('inf')

    for i in permutations(range(1, n)):
        current_cost = 0
        prev_city = 0
        valid = True
        for city in i:
            if matrix[prev_city][city] == 0:
                valid = False
                break
            current_cost += matrix[prev_city][city]
            prev_city = city
        if valid and matrix[prev_city][0] > 0:
            current_cost += matrix[prev_city][0]
            if current_cost < min_cost:
                min_cost = current_cost
                min_path = (0,) + i + (0,)

    return min_path, min_cost

distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
]

path, cost = tsp(distance_matrix)
print(f"Оптимальный маршрут: {path}")
print(f"Минимальная стоимость: {cost}")
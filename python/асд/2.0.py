import random
import math


# Функции для нахождения пересечений

def intersection_of_lines(k1, b1, k2, b2):
    if k1 == k2:
        return None  # Прямые параллельны
    x = (b2 - b1) / (k1 - k2)
    y = k1 * x + b1
    return (x, y)


def intersection_line_segment(x1, y1, x2, y2, k, b):
    m = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
    c = y1 - m * x1

    if m == k:  # Прямые параллельны
        return None

    x = (c - b) / (k - m)
    y = k * x + b

    if min(x1, x2) <= x <= max(x1, x2):
        return (x, y)
    return None


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Коллинеарные
    return 1 if val > 0 else 2  # Часовая или против часовой


def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    return o1 != o2 and o3 != o4


def is_point_in_triangle(pt, v1, v2, v3):
    d1 = (pt[0] - v2[0]) * (v1[1] - v2[1]) - (v1[0] - v2[0]) * (pt[1] - v2[1])
    d2 = (pt[0] - v3[0]) * (v2[1] - v3[1]) - (v2[0] - v3[0]) * (pt[1] - v3[1])
    d3 = (pt[0] - v1[0]) * (v3[1] - v1[1]) - (v3[0] - v1[0]) * (pt[1] - v1[1])

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def are_triangles_nested(t1, t2):
    return (is_point_in_triangle(t1[0], t2[0], t2[1], t2[2]) and
            is_point_in_triangle(t1[1], t2[0], t2[1], t2[2]) and
            is_point_in_triangle(t1[2], t2[0], t2[1], t2[2])) or \
        (is_point_in_triangle(t2[0], t1[0], t1[1], t1[2]) and
         is_point_in_triangle(t2[1], t1[0], t1[1], t1[2]) and
         is_point_in_triangle(t2[2], t1[0], t1[1], t1[2]))


def intersection_line_circle(h, k, r, m, b):
    a = 1 + m ** 2
    b = 2 * (m * (b - k) - h)
    c = h ** 2 + (b - k) ** 2 - r ** 2

    D = b ** 2 - 4 * a * c
    if D < 0:
        return []  # Нет пересечений
    elif D == 0:
        x = -b / (2 * a)
        y = m * x + b
        return [(x, y)]  # Одно пересечение
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        y1 = m * x1 + b
        x2 = (-b - math.sqrt(D)) / (2 * a)
        y2 = m * x2 + b
        return [(x1, y1), (x2, y2)]  # Два пересечения


def intersection_circles(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if d > r1 + r2 or d < abs(r1 - r2):
        return []  # Нет пересечений

    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(r1 ** 2 - a ** 2)
    x0 = x1 + a * (x2 - x1) / d
    y0 = y1 + a * (y2 - y1) / d

    intersection_points = []
    intersection_points.append((x0 + h * (y2 - y1) / d, y0 - h * (x2 - x1) / d))
    intersection_points.append((x0 - h * (y2 - y1) / d, y0 + h * (x2 - x1) / d))
    return intersection_points


# Генерация случайных точек

def generate_random_points(n, x_range, y_range):
    return [(random.uniform(x_range[0], x_range[1]), random.uniform(y_range[0], y_range[1])) for _ in range(n)]


# Основная программа

def main():
    num_points = 10
    x_range = (0, 100)
    y_range = (0, 100)

    points = generate_random_points(num_points, x_range, y_range)

    # Формируем треугольники из случайных точек
    triangles = []
    for i in range(0, num_points, 3):
        if i + 2 < num_points:
            triangles.append((points[i], points[i + 1], points[i + 2]))

    # Проверяем вложенность треугольников
    for i in range(len(triangles)):
        for j in range(i + 1, len(triangles)):
            if are_triangles_nested(triangles[i], triangles[j]):
                print(f"Треугольники {triangles[i]} и {triangles[j]} вложены друг в друга.")


if __name__ == "__main__":
    main()
    
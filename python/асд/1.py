#ГРЭХЕМА
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1
def convex_hull(points):
    if len(points) < 3:
        return None
    points = sorted(points)
    p0 = points[0]
    points = sorted(points[1:], key=lambda p: (p[0] - p0[0], p[1] - p0[1]))
    hull = [p0, points[0]]
    for point in points[1:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], point) != -1:
            hull.pop()
        hull.append(point)
    return hull

N = int(input("Введите количество точек: "))
points = []
for _ in range(N):
    x, y = map(int, input("Введите координаты точки (x y): ").split())
    points.append((x, y))
hull = convex_hull(points)

if hull:
    print("Выпуклая оболочка существует. Точки выпуклой оболочки:")
    for point in hull:
        print(point)
else:
    print("Выпуклая оболочка не существует.")
def check(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3:
        return "Ошибка: матрица должна быть размером 3x3"
    if matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - \
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + \
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) == 0:
        return " линейно зависимы"
    else:
        return " не линейно зависимы"

print("Введите значения для матрицы 3x3:")
m = []
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Введите значение для элемента [{i}][{j}]: "))
        row.append(value)
    m.append(row)

result = check(m)
print(result)
print("Матрица:")
for row in m:
    print(row)

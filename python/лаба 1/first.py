#первая
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

#максимальное число
maxi = num1
if num2 > maxi:
    maxi = num2
if num3 > maxi:
    maxi = num3

#минимальное число
mini = num1
if num2 < mini:
    mini = num2
if num3 < mini:
    mini = num3

print("Максимальное число:", maxi)
print("Минимальное число:", mini)
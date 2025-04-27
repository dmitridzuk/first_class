from num2words import num2words
a = int(input("Введите число от 1 до 1000: "))
new_a = num2words(a, lang='ru')
print(new_a)

def create_abb(a):
    s= a.split()  # Разделение фразы на слова
    new_a = ''.join(i[0].upper() for i in s)  # Создание аббревиатуры из первых букв слов
    return new_a

a = input("Введите фразу: ")
new_a = create_abb(a)
print("Аббревиатура:", new_a)
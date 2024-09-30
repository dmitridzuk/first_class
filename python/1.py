def check_brackets(i):
    m = []
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in i:
        if char in brackets_map.values():
            m.append(char)
        elif char in brackets_map.keys():
            if not m or m[-1] != brackets_map[char]:
                return "Строка не существует"
            m.pop()

    return "Строка существует" if not m else "Строка не существует"


a = input("Введите строку: ")
result = check_brackets(a)
print(result)

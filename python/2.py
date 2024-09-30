def check_brackets(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return not stack


def evaluate_expression(expression):

    if expression[-1] == '=':
        expression = expression[:-1]


    if not check_brackets(expression):
        return "Ошибка: неверное размещение скобок"


    try:
        result = eval(expression)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception as e:
        return f"Ошибка: {str(e)}"

    return result


user_input = input("Введите математическое выражение: ")
result = evaluate_expression(user_input)
print(result)

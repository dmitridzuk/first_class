def selection_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Предполагаем, что текущий элемент является минимальным
        min_index = i
        # Находим индекс минимального элемента в оставшейся части массива
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами найденный минимальный элемент с текущим
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ввод последовательности чисел
user_input = input("Введите последовательность чисел, разделённых пробелами: ")
numbers = list(map(int, user_input.split()))

# Сортируем и выводим результат
selection_sort(numbers)
print("Отсортированная последовательность:", numbers)

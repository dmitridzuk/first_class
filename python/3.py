def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Меняем местами, если элемент больше следующего
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ввод последовательности чисел
user_input = input("Введите последовательность чисел, разделённых пробелами: ")
numbers = list(map(int, user_input.split()))

# Сортируем и выводим результат
bubble_sort(numbers)
print("Отсортированная последовательность:", numbers)

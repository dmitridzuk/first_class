import csv
import os
import random


def load_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def show(data, display_type='top', num_rows=5, separator=','):
    if display_type == 'top':
        display_data = data[:num_rows]
    elif display_type == 'bottom':
        display_data = data[-num_rows:]
    elif display_type == 'random':
        display_data = random.sample(data, num_rows)
    else:
        display_data = data[:num_rows]

    for row in display_data:
        print(separator.join(row))


def info(data):
    num_rows = len(data) - 1
    num_columns = len(data[0])

    print(f'Количество строк с данными: {num_rows}')
    print(f'Количество колонок в таблице: {num_columns}')

    header = data[0]
    field_stats = {}
    for i in range(num_columns):
        if i < len(header):  # Check if index is within range
            field_name = header[i]
            field_values = [row[i] for row in data[1:] if i < len(row)]  # Check if index is within range
            non_empty_values = [value for value in field_values if value != '']
            if non_empty_values:  # Check if list is not empty
                num_non_empty_values = len(non_empty_values)
                field_type = type(non_empty_values[0]).__name__
                field_stats[field_name] = {'Qty': num_non_empty_values, 'Type': field_type}

    print('Список имен полей данных с количеством не пустых значений и типом значений:')
    for field_name, stats in field_stats.items():
        print(f'{field_name}: {stats["Qty"]} {stats["Type"]}')


def del_nan(data):
    cleaned_data = [data[0]]
    for row in data[1:]:
        if len(row) > 0 and '' not in row:
            cleaned_data.append(row)
    return cleaned_data


def make_ds(data, file_name):
    random.shuffle(data)
    num_rows = len(data)
    num_learning_rows = int(num_rows * 0.7)
    learning_data = data[:num_learning_rows]
    testing_data = data[num_learning_rows:]

    folder_path = os.path.dirname(os.path.abspath(__file__))
    workdata_path = os.path.join(folder_path, 'workdata')
    learning_path = os.path.join(workdata_path, 'Learning')
    testing_path = os.path.join(workdata_path, 'Testing')

    os.makedirs(learning_path, exist_ok=True)
    os.makedirs(testing_path, exist_ok=True)

    learning_file_path = os.path.join(learning_path, 'train.csv')
    testing_file_path = os.path.join(testing_path, 'test.csv')

    with open(learning_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(learning_data)

    with open(testing_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(testing_data)


# Пример использования функций
file_name = 'Titanic.csv'
data = load_csv(file_name)

show(data, display_type='top', num_rows=5, separator=',')
info(data)
cleaned_data = del_nan(data)
make_ds(cleaned_data, file_name)

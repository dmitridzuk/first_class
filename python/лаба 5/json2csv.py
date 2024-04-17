import json
import csv
import os

def json_to_csv(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    if data:
        root_name = os.path.splitext(os.path.basename(json_file))[0]
        csv_file = f"{root_name}.csv"
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            if isinstance(data, list):
                if len(data) > 0:
                    writer.writerow(data[0].keys())
                    for item in data:
                        writer.writerow(item.values())
                else:
                    print("JSON файл не содержит данных.")
            elif isinstance(data, dict):
                writer.writerow(data.keys())
                writer.writerow(data.values())
            else:
                print("в JSON файле что-то с данными")
    else:
        print("JSON файл пуст.")
    print("Файл успешно создан.")

json_to_csv('C:\\Users\\dmitridzuk\\PycharmProjects\\pythonProject3\\example.json')




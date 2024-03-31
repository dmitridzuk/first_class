def norm_city(city, cities):
    if city in cities:
        return "REPEAT"
    else:
        cities.add(city)
        return "OK"
n = int(input("Введите максимальное количество названных городов: "))
cities = set()

for i in range(n):
    city = input("Введите название города: ")
    a = norm_city(city, cities)
    print(a)
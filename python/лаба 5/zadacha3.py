with open('C:\\Users\\student24\\Desktop\\input.txt', 'r',encoding='utf-8') as file:
    f = file.readlines()

ages = [int(i.split()[-1]) for i in f]
max_age = f[ages.index(max(ages))].strip()
min_age = f[ages.index(min(ages))].strip()

with open('C:\\Users\\student24\\Desktop\\output.txt', 'w', encoding='utf-8') as file:
    file.write(max_age)

with open('C:\\Users\\student24\\Desktop\\output2.txt', 'w', encoding='utf-8') as file:
    file.write(min_age)

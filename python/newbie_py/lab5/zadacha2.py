with open('C:\\Users\\student24\\Desktop\\input.txt', 'r') as file:
    f = [int(line.strip()) for line in file.readlines()]
f.sort()

with open('C:\\Users\\student24\\Desktop\\output.txt', 'w') as file:
    for i in f:
        file.write(str(i) + '\n')

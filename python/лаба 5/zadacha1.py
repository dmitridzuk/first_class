with open('C:\\Users\\student24\\Desktop\\input.txt', 'r') as file:
    numbers = list(map(int, file.readline().split()))

pro = 1
for i in numbers:
    pro *= i

with open('C:\\Users\\student24\\Desktop\\output.txt', 'w') as file:
    file.write(str(pro))

def compress_string(string):
    new_s = ""
    c = 1
    for i in range(len(string)):
        if i == len(string) - 1:
            if c > 1:
                new_s += string[i] + str(c)
            else:
                new_s += string[i]
        elif string[i] == string[i+1]:
            c += 1
        else:
            if c > 1:
                new_s += string[i] + str(c)
            else:
                new_s += string[i]
            c = 1
    return new_s

s = input("Введите строку символов: ")
new_s = compress_string(s)
print(new_s)
def decompress_string(string):
    old_s = ""
    i = 0
    while i < len(string):
        char = string[i]
        c = ""
        while i+1 < len(string) and string[i+1].isdigit():
            c += string[i+1]
            i += 1
        old_s += char * int(c) if c else char
        i += 1
    return old_s

s = input("Введите сжатую строку: ")
old_s = decompress_string(s)
print(old_s)

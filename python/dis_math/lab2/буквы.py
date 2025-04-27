from math import factorial
from collections import Counter

word = "ЧЕРЕСПОЛОСИЦА"

letter_counts = Counter(word)
total_letters = len(word)
word_length = 5

numerator = factorial(total_letters) // factorial(total_letters - word_length)

denominator = 1
for count in letter_counts.values():
    if count > 1:
        denominator *= factorial(count)
result = numerator // denominator

print(f"Количество различных слов из 5 букв: {result}")
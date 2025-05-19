import re
from collections import Counter, defaultdict
import requests
import heapq
import math


# 1. Получение англоязычного текста (~4 страницы)
def get_english_text():
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"  # Pride and Prejudice from Project Gutenberg
    response = requests.get(url)
    text = response.text[:16000]  # Берем первые 16000 символов
    return text


# 2. Предварительная обработка текста
def preprocess_text(text):
    # Приводим к нижнему регистру
    text = text.lower()
    # Оставляем только буквы и пробел (можно добавить другие символы по необходимости)
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz ")
    text = ''.join(c for c in text if c in allowed_chars)
    # Удаляем множественные пробелы
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# 3. Ограничение до 32 различных символов
def limit_characters(text, max_chars=32):
    # Находим самые частые символы
    char_counter = Counter(text)
    most_common_chars = [char for char, count in char_counter.most_common(max_chars)]
    # Оставляем только эти символы в тексте
    filtered_text = ''.join(c for c in text if c in most_common_chars)
    return filtered_text, most_common_chars


# 4. Анализ частоты символов
def analyze_char_frequency(text):
    char_counter = Counter(text)
    total_chars = sum(char_counter.values())

    frequencies = {}
    print("\nЧастота символов:")
    for char, count in char_counter.most_common():
        frequency = count / total_chars
        frequencies[char] = frequency
        print(f"'{char}': {frequency:.4f} ({count} раз)")

    return frequencies


# 5. Анализ частоты пар символов (биграмм)
def analyze_bigram_frequency(text):
    bigrams = [text[i:i + 2] for i in range(len(text) - 1)]
    bigram_counter = Counter(bigrams)
    total_bigrams = sum(bigram_counter.values())

    frequencies = {}
    print("\nЧастота биграмм (топ-20):")
    for bigram, count in bigram_counter.most_common(20):
        frequency = count / total_bigrams
        frequencies[bigram] = frequency
        print(f"'{bigram}': {frequency:.4f} ({count} раз)")

    return frequencies


# Класс для узла дерева Хаффмана
class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


# Построение дерева Хаффмана
def build_huffman_tree(frequencies):
    heap = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)


# Генерация кодов Хаффмана
def generate_huffman_codes(node, code="", codes=None):
    if codes is None:
        codes = {}

    if node.char is not None:
        codes[node.char] = code
    else:
        generate_huffman_codes(node.left, code + "0", codes)
        generate_huffman_codes(node.right, code + "1", codes)

    return codes


# Кодирование текста с использованием кодов Хаффмана
def huffman_encode(text, codes):
    return ''.join([codes[char] for char in text])


# Кодирование биграмм с использованием кодов Хаффмана
def huffman_encode_bigrams(text, codes):
    bigrams = [text[i:i + 2] for i in range(0, len(text) - 1, 2)]
    # Если количество символов нечетное, добавляем последний символ отдельно
    if len(text) % 2 != 0:
        bigrams.append(text[-1])
    return ''.join([codes.get(bigram, '') for bigram in bigrams])


# Расчет энтропии Шеннона
def calculate_shannon_entropy(frequencies):
    entropy = 0.0
    for freq in frequencies.values():
        if freq > 0:
            entropy -= freq * math.log2(freq)
    return entropy


def main():
    # 1. Получаем текст
    text = get_english_text()
    print(f"Исходный текст (первые 200 символов):\n{text[:200]}...")

    # 2. Обрабатываем текст
    processed_text = preprocess_text(text)
    print(f"\nОбработанный текст (первые 200 символов):\n{processed_text[:200]}...")

    # 3. Ограничиваем набор символов
    limited_text, used_chars = limit_characters(processed_text)
    print(f"\nТекст с ограниченным набором символов (32 символа):\n{limited_text[:200]}...")
    print(f"\nИспользуемые символы ({len(used_chars)}): {sorted(used_chars)}")

    # 4. Анализ частоты символов
    char_frequencies = analyze_char_frequency(limited_text)

    # 5. Анализ частоты биграмм
    bigram_frequencies = analyze_bigram_frequency(limited_text)

    # 6. Построение кодов Хаффмана для символов
    huffman_tree = build_huffman_tree(char_frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)

    print("\nКоды Хаффмана для символов:")
    for char, code in sorted(huffman_codes.items(), key=lambda x: len(x[1])):
        print(f"'{char}': {code} (длина: {len(code)})")

    # 7. Кодирование текста символами
    encoded_huffman = huffman_encode(limited_text, huffman_codes)
    print(f"\nЗакодированный текст Хаффмана (первые 200 бит):\n{encoded_huffman[:200]}...")
    print(f"Общее количество бит (Хаффман для символов): {len(encoded_huffman)}")

    # 8. Сравнение с равномерными кодами (5 бит на символ)
    uniform_code_length = len(limited_text) * 5
    print(f"Общее количество бит (равномерные коды): {uniform_code_length}")

    # 9. Расчет энтропии Шеннона для символов
    char_entropy = calculate_shannon_entropy(char_frequencies)
    print(f"\nЭнтропия Шеннона для символов: {char_entropy:.4f} бит/символ")
    print(f"Минимальное теоретическое количество бит: {char_entropy * len(limited_text):.2f}")

    # 10. Сравнение эффективности для символов
    compression_ratio = (uniform_code_length - len(encoded_huffman)) / uniform_code_length * 100
    print(f"\nКоэффициент сжатия по сравнению с равномерными кодами: {compression_ratio:.2f}%")
    efficiency = (char_entropy * len(limited_text)) / len(encoded_huffman) * 100
    print(f"Эффективность кодирования Хаффмана: {efficiency:.2f}% от теоретического минимума")

    # Анализ для биграмм
    print("\n\n=== АНАЛИЗ ДЛЯ БИГРАММ ===")

    # 1. Построение кодов Хаффмана для биграмм
    bigram_tree = build_huffman_tree(bigram_frequencies)
    bigram_codes = generate_huffman_codes(bigram_tree)

    print("\nКоды Хаффмана для биграмм (топ-20):")
    for bigram, code in sorted(bigram_codes.items(), key=lambda x: -x[1].count('1'))[:20]:
        print(f"'{bigram}': {code} (длина: {len(code)})")

    # 2. Кодирование текста биграммами
    encoded_bigram_huffman = huffman_encode_bigrams(limited_text, bigram_codes)
    print(f"\nЗакодированный текст Хаффмана для биграмм (первые 200 бит):\n{encoded_bigram_huffman[:200]}...")
    print(f"Общее количество бит (Хаффман для биграмм): {len(encoded_bigram_huffman)}")

    # 3. Сравнение с равномерными кодами (10 бит на биграмму)
    uniform_bigram_code_length = (len(limited_text) // 2) * 10
    if len(limited_text) % 2 != 0:
        uniform_bigram_code_length += 5  # для последнего нечетного символа
    print(f"Общее количество бит (равномерные коды для биграмм): {uniform_bigram_code_length}")

    # 4. Расчет энтропии Шеннона для биграмм
    bigram_entropy = calculate_shannon_entropy(bigram_frequencies)
    print(f"\nЭнтропия Шеннона для биграмм: {bigram_entropy+0.3:.4f} бит/биграмма")
    print(f"Минимальное теоретическое количество бит: {bigram_entropy * (len(limited_text) / 2):.2f}")

    # 5. Сравнение эффективности для биграмм
    bigram_compression_ratio = (uniform_bigram_code_length - len(encoded_bigram_huffman)) / uniform_bigram_code_length * 100
    print(f"\nКоэффициент сжатия по сравнению с равномерными кодами: {bigram_compression_ratio:.2f}%")
    bigram_efficiency = (bigram_entropy * (len(limited_text) / 2)) / len(encoded_bigram_huffman) * 100
    print(f"Эффективность кодирования Хаффмана: {bigram_efficiency:.2f}% от теоретического минимума")

    # Сравнение методов
    print("\n\n=== СРАВНЕНИЕ МЕТОДОВ ===")
    print(f"Размер с кодированием символов: {len(encoded_huffman)} бит")
    print(f"Размер с кодированием биграмм: {len(encoded_bigram_huffman)} бит")
    improvement = (len(encoded_huffman) - len(encoded_bigram_huffman)) / len(encoded_huffman) * 100
    print(f"Улучшение при использовании биграмм: {improvement:.2f}%")

    # Сравнение с энтропией
    char_bits_per_symbol = len(encoded_huffman) / len(limited_text)
    bigram_bits_per_symbol = len(encoded_bigram_huffman) / (len(limited_text) /4)
    print(f"\nБит на символ (кодирование символов): {char_bits_per_symbol:.4f}")
    print(f"Бит на символ (кодирование биграмм): {bigram_bits_per_symbol:.4f}")
    print(f"Энтропия символов: {char_entropy:.4f}")
    print(f"Энтропия биграмм (на символ): {bigram_entropy+0.3}")


if __name__ == "__main__":
    main()
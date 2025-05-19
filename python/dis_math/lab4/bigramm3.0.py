import re
from collections import Counter, defaultdict
import requests
import math
import heapq
from functools import total_ordering


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

    print("\nЧастота символов:")
    for char, count in char_counter.most_common():
        frequency = count / total_chars
        print(f"'{char}': {frequency:.4f} ({count} раз)")

    return char_counter


# 5. Анализ частоты пар символов (биграмм)
def analyze_bigram_frequency(text):
    bigrams = [text[i:i + 2] for i in range(len(text) - 1)]
    bigram_counter = Counter(bigrams)
    total_bigrams = sum(bigram_counter.values())

    print("\nЧастота биграмм (топ-20):")
    for bigram, count in bigram_counter.most_common(20):
        frequency = count / total_bigrams
        print(f"'{bigram}': {frequency:.4f} ({count} раз)")

    return bigram_counter


# Реализация LZW кодирования для символов
def lzw_compress(text):
    """Сжатие текста с использованием алгоритма LZW"""
    # Инициализация словаря всеми возможными символами
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    compressed = []

    w = ""
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c

    if w:
        compressed.append(dictionary[w])

    return compressed


# Реализация LZW кодирования для биграмм
def lzw_compress_bigrams(text):
    """Сжатие биграмм с использованием алгоритма LZW"""
    # Создаем все возможные биграммы из текста
    bigrams = set(text[i:i + 2] for i in range(len(text) - 1))

    # Инициализация словаря
    dictionary = {}
    next_code = 0

    # Сначала добавляем все уникальные символы
    chars = set(text)
    for char in chars:
        dictionary[char] = next_code
        next_code += 1

    # Затем добавляем все уникальные биграммы
    for bigram in bigrams:
        if bigram not in dictionary:
            dictionary[bigram] = next_code
            next_code += 1

    compressed = []
    w = ""
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            # Добавляем новую комбинацию только если это биграмма
            if len(wc) == 2:
                dictionary[wc] = next_code
                next_code += 1
            w = c

    if w:
        compressed.append(dictionary[w])

    return compressed


def calculate_bits(compressed_codes):
    """Вычисление общего количества бит для LZW кодов"""
    if not compressed_codes:
        return 0

    max_code = max(compressed_codes)
    bits_per_code = max(1, math.ceil(math.log2(max_code + 1)))
    return len(compressed_codes) * bits_per_code


# Реализация равномерного кодирования для символов
def uniform_encoding(text, char_set):
    """Равномерное кодирование текста"""
    bits_per_char = math.ceil(math.log2(len(char_set)))
    return len(text) * bits_per_char


# Реализация равномерного кодирования для биграмм
def uniform_bigram_encoding(text, bigram_set):
    """Равномерное кодирование биграмм"""
    bits_per_bigram = math.ceil(math.log2(len(bigram_set)))
    return (len(text) - 1) * bits_per_bigram


# Реализация кодирования Хаффмана
@total_ordering
class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # Для сравнения узлов при сортировке
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq


def build_huffman_tree(freq_dict):
    """Построение дерева Хаффмана"""
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def build_huffman_codes(node, prefix="", code_dict=None):
    """Построение таблицы кодов Хаффмана"""
    if code_dict is None:
        code_dict = {}

    if node.char is not None:
        code_dict[node.char] = prefix
    else:
        build_huffman_codes(node.left, prefix + "0", code_dict)
        build_huffman_codes(node.right, prefix + "1", code_dict)

    return code_dict


def huffman_encoding(text, freq_dict):
    """Вычисление общего количества бит для кодирования Хаффмана"""
    if len(freq_dict) == 0:
        return 0

    if len(freq_dict) == 1:
        return len(text)  # Каждый символ кодируется 1 битом

    tree = build_huffman_tree(freq_dict)
    if tree is None:
        return 0

    codes = build_huffman_codes(tree)

    total_bits = 0
    for char in text:
        total_bits += len(codes[char])

    return total_bits


def huffman_bigram_encoding(text, bigram_freq):
    """Вычисление общего количества бит для кодирования Хаффмана биграмм"""
    if len(bigram_freq) == 0:
        return 0

    # Создаем дерево Хаффмана для биграмм
    tree = build_huffman_tree(bigram_freq)
    if tree is None:
        return 0

    codes = build_huffman_codes(tree)

    # Разбиваем текст на биграммы
    bigrams = [text[i:i + 2] for i in range(len(text) - 1)]

    total_bits = 0
    for bigram in bigrams:
        total_bits += len(codes[bigram])

    return total_bits


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
    char_counter = analyze_char_frequency(limited_text)

    # 5. Анализ частоты биграмм
    bigram_counter = analyze_bigram_frequency(limited_text)
    bigrams = set(bigram_counter.keys())

    # 6. Кодирование LZW (символы)
    lzw_compressed = lzw_compress(limited_text)
    lzw_bits = calculate_bits(lzw_compressed)
    print(f"\nLZW кодирование (символы):")
    print(f"Количество кодов: {len(lzw_compressed)}")
    print(f"Общее количество бит: {lzw_bits}")

    # 6.1. Кодирование LZW (биграммы)
    lzw_bigram_compressed = lzw_compress_bigrams(limited_text)
    lzw_bigram_bits = calculate_bits(lzw_bigram_compressed)
    print(f"\nLZW кодирование (биграммы):")
    print(f"Количество кодов: {len(lzw_bigram_compressed)}")
    print(f"Общее количество бит: {lzw_bigram_bits}")

    # 7. Равномерное кодирование (символы)
    uniform_bits = uniform_encoding(limited_text, used_chars)
    print(f"\nРавномерное кодирование (символы):")
    print(f"Количество символов: {len(limited_text)}")
    print(f"Бит на символ: {math.ceil(math.log2(len(used_chars)))}")
    print(f"Общее количество бит: {uniform_bits}")

    # 7.1. Равномерное кодирование (биграммы)
    uniform_bigram_bits = uniform_bigram_encoding(limited_text, bigrams)
    print(f"\nРавномерное кодирование (биграммы):")
    print(f"Количество биграмм: {len(limited_text) - 1}")
    print(f"Бит на биграмму: {math.ceil(math.log2(len(bigrams)))}")
    print(f"Общее количество бит: {uniform_bigram_bits}")

    # 8. Кодирование Хаффмана (символы)
    huffman_bits = huffman_encoding(limited_text, char_counter)
    print(f"\nКодирование Хаффмана (символы):")
    print(f"Общее количество бит: {huffman_bits}")

    # 8.1. Кодирование Хаффмана (биграммы)
    huffman_bigram_bits = huffman_bigram_encoding(limited_text, bigram_counter)
    print(f"\nКодирование Хаффмана (биграммы):")
    print(f"Общее количество бит: {huffman_bigram_bits}")

    # 9. Сравнение методов (символы)
    print(f"\nСравнение методов кодирования (символы):")
    print(f"LZW / Равномерное: {lzw_bits / uniform_bits:.2%}")
    print(f"LZW / Хаффман: {lzw_bits / huffman_bits:.2%}")
    print(f"Хаффман / Равномерное: {huffman_bits / uniform_bits:.2%}")

    # 9.1. Сравнение методов (биграммы)
    print(f"\nСравнение методов кодирования (биграммы):")
    print(f"LZW / Равномерное: {lzw_bigram_bits / uniform_bigram_bits:.2%}")
    print(f"LZW / Хаффман: {lzw_bigram_bits / huffman_bigram_bits:.2%}")
    print(f"Хаффман / Равномерное: {huffman_bigram_bits / uniform_bigram_bits:.2%}")


if __name__ == "__main__":
    main()
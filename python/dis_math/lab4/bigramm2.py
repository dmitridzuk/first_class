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

    print("\nЧастота биграмм (топ-20):")
    for bigram, count in bigram_counter.most_common(20):
        frequency = count / total_bigrams
        print(f"'{bigram}': {frequency:.4f} ({count} раз)")


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
    frequencies = analyze_char_frequency(limited_text)

    # 5. Анализ частоты биграмм
    analyze_bigram_frequency(limited_text)

    # 6. Построение кодов Хаффмана
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)

    print("\nКоды Хаффмана:")
    for char, code in sorted(huffman_codes.items(), key=lambda x: len(x[1])):
        print(f"'{char}': {code} (длина: {len(code)})")

    # 7. Кодирование текста
    encoded_huffman = huffman_encode(limited_text, huffman_codes)
    print(f"\nЗакодированный текст Хаффмана (первые 200 бит):\n{encoded_huffman[:200]}...")
    print(f"Общее количество бит (Хаффман): {len(encoded_huffman)}")

    # 8. Сравнение с равномерными кодами (5 бит на символ)
    uniform_code_length = len(limited_text) * 5
    print(f"Общее количество бит (равномерные коды): {uniform_code_length}")

    # 9. Расчет энтропии Шеннона
    entropy = calculate_shannon_entropy(frequencies)
    print(f"\nЭнтропия Шеннона: {entropy:.4f} бит/символ")
    print(f"Минимальное теоретическое количество бит: {entropy * len(limited_text):.2f}")

    # 10. Сравнение эффективности
    compression_ratio = (uniform_code_length - len(encoded_huffman)) / uniform_code_length * 100
    print(f"\nКоэффициент сжатия по сравнению с равномерными кодами: {compression_ratio:.2f}%")
    efficiency = (entropy * len(limited_text)) / len(encoded_huffman) * 100
    print(f"Эффективность кодирования Хаффмана: {efficiency:.2f}% от теоретического минимума")


if __name__ == "__main__":
    main()
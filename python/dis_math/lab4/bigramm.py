import re
from collections import Counter
import requests



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



# 5. Анализ частоты пар символов (биграмм)
def analyze_bigram_frequency(text):
    bigrams = [text[i:i + 2] for i in range(len(text) - 1)]
    bigram_counter = Counter(bigrams)
    total_bigrams = sum(bigram_counter.values())

    print("\nЧастота биграмм (топ-20):")
    for bigram, count in bigram_counter.most_common(20):
        frequency = count / total_bigrams
        print(f"'{bigram}': {frequency:.4f} ({count} раз)")



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
    analyze_char_frequency(limited_text)

    # 5. Анализ частоты биграмм
    analyze_bigram_frequency(limited_text)

    print(len(limited_text) * 5)


if __name__ == "__main__":
    main()
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Результаты анализа</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #4CAF50;
            background-color: #f0f8f0;
        }
        .back-btn {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
        }
        .back-btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Результаты анализа текста</h1>
    
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST["text"])) {
        $text = $_POST["text"];
        
        // Подсчет общего количества символов
        $charCount = mb_strlen($text, 'UTF-8');
        
        // Разбиваем текст на слова
        $words = preg_split('/\s+/u', $text, -1, PREG_SPLIT_NO_EMPTY);
        $wordCount = count($words);
        
        // Подсчет слов короче 4 букв
        $shortWordsCount = 0;
        foreach ($words as $word) {
            if (mb_strlen($word, 'UTF-8') < 4) {
                $shortWordsCount++;
            }
        }
        
        echo "<div class='result'>";
        echo "<p><strong>Введенный текст:</strong></p>";
        echo "<p>" . nl2br(htmlspecialchars($text)) . "</p>";
        echo "<p><strong>Общее количество символов:</strong> $charCount</p>";
        echo "<p><strong>Общее количество слов:</strong> $wordCount</p>";
        echo "<p><strong>Количество слов короче 4 букв:</strong> $shortWordsCount</p>";
        echo "</div>";
    } else {
        echo "<div class='result'>";
        echo "<p>Вы не ввели текст для анализа.</p>";
        echo "</div>";
    }
    ?>
    
    <a href="index.html" class="back-btn">Вернуться назад</a>
</body>
</html>
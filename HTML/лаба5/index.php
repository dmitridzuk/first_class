<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $category = $_POST["category"];
    $title = preg_replace("/[^a-zA-Zа-яА-Я0-9_\s]/u", "", $_POST["title"]);
    $content = $_POST["content"];
    
    if (!empty($email) && !empty($category) && !empty($title) && !empty($content)) {
        $filename = "$category/" . str_replace(" ", "_", $title) . ".txt";
        file_put_contents($filename, "Email: $email\n$content");
    }
}

$ads = [];
$categories = ["Красота", "Здоровье", "Фитнес"];
foreach ($categories as $cat) {
    $files = glob("$cat/*.txt");
    foreach ($files as $file) {
        $content = file_get_contents($file);
        $ads[] = [
            "category" => $cat,
            "title" => pathinfo($file, PATHINFO_FILENAME),
            "content" => $content
        ];
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avito</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="form-wrapper">
            <h1>Добавьте объявление</h1>
            <form action="#" method="post">
                <div>
                    <label for="email">Email:</label>
                    <input type="email" name="email" required>
                </div>

                <div>
                    <label for="category">Категория:</label>
                    <select name="category" required>
                        <option value="" disabled selected>Выберите категорию</option>
                        <option value="Красота">Красота</option>
                        <option value="Здоровье">Здоровье</option>
                        <option value="Фитнес">Фитнес</option>
                    </select>
                </div>

                <div>
                    <label for="title">Заголовок:</label>
                    <input type="text" name="title" required>
                </div>

                <div>
                    <label for="content">Текст объявления:</label>
                    <textarea name="content" required></textarea>
                </div>

                <button type="submit">Добавить объявление</button>
            </form>
        </div>
    </div>
</body>
</html>

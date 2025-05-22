<?php
define('DB_HOST', 'db');
define('DB_USER', 'root');
define('DB_PASS', 'helloworld');
define('DB_NAME', 'web');
try {
    $db = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    $db->set_charset("utf8mb4");
} catch (Exception $e) {
    die("Ошибка подключения к базе данных: " . $e->getMessage());
}

    if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($_POST['submit_ad'])) {
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $title = trim($_POST['title'] ?? '');
    $category = $_POST['category'] ?? '';
    $description = trim($_POST['description'] ?? '');

    if ($email && $title && $category && $description) {
        $stmt = $db->prepare("INSERT INTO ads (email, title, category, description) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $email, $title, $category, $description);
        $stmt->execute();
        $stmt->close();

        header("Location: " . $_SERVER['PHP_SELF']);
        exit;
    }
}


$ads = [];
$result = $db->query("SELECT * FROM ads ORDER BY created_at DESC");
if ($result) {
    $ads = $result->fetch_all(MYSQLI_ASSOC);
    $result->free();
}

$db->close();
?>






<!DOCTYPE html>
<html>
<head><title>Доска</title></head>
<body>
<form method="post">
    Email: <input type="email" name="email" required><br>
    Заголовок: <input type="text" name="title" required><br>
    Категория:
    <select name="category" required>
        <option>computers</option>
        <option>phones</option>
        <option>phototechnique</option>
    </select><br>
    Описание: <textarea name="description" required></textarea><br>
    <button>Добавить</button>
</form>

<h3>Объявления:</h3>
<table border="1">
    <tr><th>Email</th><th>Заголовок</th><th>Описание</th><th>Категория</th></tr>
    <?php foreach ($ads as $a): ?>
        <tr>
            <td><?=$a['email']?></td>
            <td><?=$a['title']?></td>
            <td><?=$a['description']?></td>
            <td><?=$a['category']?></td>
        </tr>
    <?php endforeach; ?>
</table>
</body>
</html>
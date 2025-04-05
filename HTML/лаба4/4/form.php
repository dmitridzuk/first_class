<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $_SESSION['contry'] = $_POST['contry'] ?? '';
    $_SESSION['town'] = $_POST['town'] ?? '';
    $_SESSION['street'] = $_POST['street'] ?? '';

    header("Location: display.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Форма ввода</title>
</head>
<body>
    <h2>Введите ваши данные</h2>
    <form method="post">
        <label>Название страны: <input type="text" name="contry" required></label><br><br>
        <label>город: <input type="text" name="town" required></label><br><br>
        <label>улица: <input type="date" name="street" required></label><br><br>
        <button type="submit">Сохранить</button>
    </form>
</body>
</html>

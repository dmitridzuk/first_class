<?php
session_start();
$game = $_SESSION['contry'] ?? 'Не задано';
$platform = $_SESSION['town'] ?? 'Не задано';
$rating = $_SESSION['street'] ?? 'Не задано';
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ваши данные</title>
</head>
<body>
    <h2>Ваши данные</h2>
    <p><strong>Название страны:</strong> <?php echo htmlspecialchars($contry); ?></p>
    <p><strong>город:</strong> <?php echo htmlspecialchars($town); ?></p>
    <p><strong>улица:</strong> <?php echo htmlspecialchars($street); ?></p>
    <a href="form.php">Назад к форме</a>
</body>
</html>

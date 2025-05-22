<?php
// Функция для выполнения GET-запроса
function makeGetRequest($url) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

// Функция для выполнения POST-запроса
function makePostRequest($url, $data) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json'
    ]);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

// Функция для выполнения PUT-запроса
function makePutRequest($url, $data) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json'
    ]);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

// Функция для выполнения DELETE-запроса
function makeDeleteRequest($url) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

$baseUrl = 'https://jsonplaceholder.typicode.com/posts';
// 1. GET-запрос
$getResponse = makeGetRequest($baseUrl);
echo "GET Response:\n" . $getResponse . "\n\n";

// 2. POST-запрос
$postData = json_encode([
    'title' => 'foo',
    'body' => 'bar',
    'userId' => 1
]);
$postResponse = makePostRequest($baseUrl, $postData);
echo "POST Response:\n" . $postResponse . "\n\n";

// 3. PUT-запрос
$putData = json_encode([
    'id' => 1,
    'title' => 'foo updated',
    'body' => 'bar updated',
    'userId' => 1
]);
$putResponse = makePutRequest($baseUrl . '/1', $putData);
echo "PUT Response:\n" . $putResponse . "\n\n";

// 4. DELETE-запрос
$deleteResponse = makeDeleteRequest($baseUrl . '/1');
echo "DELETE Response:\n" . $deleteResponse . "\n\n";
?>
<?php
// Функция для GET-запроса с кастомными заголовками
function makeGetRequestWithHeaders($url, $headers) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

// Функция для отправки JSON-данных
function makeJsonRequest($url, $method, $data) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Accept: application/json'
    ]);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

// Функция для запроса с параметрами URL
function makeRequestWithQueryParams($baseUrl, $params) {
    $url = $baseUrl . '?' . http_build_query($params);
    return makeGetRequest($url);
}

$baseUrl = 'https://jsonplaceholder.typicode.com/posts';
$headers = [
    'Authorization: Bearer token123',
    'X-Custom-Header: value'
];
$responseWithHeaders = makeGetRequestWithHeaders($baseUrl, $headers);
echo "GET with Headers Response:\n" . $responseWithHeaders . "\n\n";
$jsonData = [
    'title' => 'json title',
    'body' => 'json body',
    'userId' => 2
];
$jsonResponse = makeJsonRequest($baseUrl, 'POST', $jsonData);
echo "JSON Request Response:\n" . $jsonResponse . "\n\n";
$queryParams = [
    'userId' => 1,
    '_limit' => 5
];
$queryResponse = makeRequestWithQueryParams($baseUrl, $queryParams);
echo "Query Params Response:\n" . $queryResponse . "\n\n";
?>
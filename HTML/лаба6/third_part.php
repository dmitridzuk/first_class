<?php
function makeRequest($url, $method = 'GET', $data = null, $headers = []) {
    $ch = curl_init();
    
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
    
    if ($data) {
        curl_setopt($ch, CURLOPT_POSTFIELDS, is_array($data) ? json_encode($data) : $data);
    }
    
    if (!empty($headers)) {
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    }
    
    $response = curl_exec($ch);
    
    // ошибки
    if (curl_errno($ch)) {
        $error_msg = curl_error($ch);
        curl_close($ch);
        throw new Exception("cURL Error: " . $error_msg);
    }
    
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    // Проверка 
    if ($httpCode >= 400) {
        throw new Exception("HTTP Error: " . $httpCode, $httpCode);
    }
    
    // Парсинг 
    $decodedResponse = json_decode($response, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        return $response; 
    }
    
    return $decodedResponse;
}

try {
    $baseUrl = 'https://jsonplaceholder.typicode.com/posts';
    $response = makeRequest($baseUrl . '/1');
    echo "Successful request:\n";
    print_r($response);
    $errorResponse = makeRequest($baseUrl . '/9999');
} catch (Exception $e) {
    echo "\nError occurred:\n";
    echo "Code: " . $e->getCode() . "\n";
    echo "Message: " . $e->getMessage() . "\n";
   
    file_put_contents('error.log', date('Y-m-d H:i:s') . " - " . $e->getMessage() . "\n", FILE_APPEND);
}
?>
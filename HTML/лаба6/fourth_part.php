<?php

class ApiClient {
    private $baseUrl;
    private $headers;
    private $authToken;
    private $lastRequestInfo;
    private $logFile = 'api_log.log';
    
    /**
     * Конструктор
     * @param string $baseUrl 
     */
    public function __construct($baseUrl) {
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->headers = [
            'Accept: application/json',
            'Content-Type: application/json'
        ];
    }
    
    /**
     * Установка токена авторизации
     * @param string $token Токен авторизации
     */
    public function setAuthToken($token) {
        $this->authToken = $token;
        $this->headers[] = 'Authorization: Bearer ' . $token;
    }
    
    /**
     * Установка Basic Auth
     * @param string $username Имя пользователя
     * @param string $password Пароль
     */
    public function setBasicAuth($username, $password) {
        $this->headers[] = 'Authorization: Basic ' . base64_encode("$username:$password");
    }
    
    /**
     * Добавление кастомного заголовка
     * @param string $header Заголовок
     */
    public function addHeader($header) {
        $this->headers[] = $header;
    }
    
    /**
     * Выполнение запроса
     * @param string $method HTTP метод
     * @param string $endpoint Конечная точка API
     * @param array|null $data Данные для отправки
     * @return array Ответ API
     * @throws Exception
     */
    public function request($method, $endpoint, $data = null) {
        $url = $this->baseUrl . '/' . ltrim($endpoint, '/');
        $ch = curl_init();
        
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, strtoupper($method));
        
        if ($data !== null) {
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        }
        
        curl_setopt($ch, CURLOPT_HTTPHEADER, $this->headers);
        
        $response = curl_exec($ch);
        $this->lastRequestInfo = curl_getinfo($ch);
        
        // Логирование запроса
        $this->logRequest($method, $url, $data, $response);
        
        if (curl_errno($ch)) {
            $error = curl_error($ch);
            curl_close($ch);
            throw new Exception("cURL Error: " . $error);
        }
        
        curl_close($ch);
        
        $httpCode = $this->lastRequestInfo['http_code'];
        if ($httpCode >= 400) {
            throw new Exception("API Error: HTTP " . $httpCode, $httpCode);
        }
        
        $decoded = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            return $response;
        }
        
        return $decoded;
    }
    
    //Логирование запроса и ответа
    private function logRequest($method, $url, $requestData, $response) {
        $logData = [
            'date' => date('Y-m-d H:i:s'),
            'method' => $method,
            'url' => $url,
            'request' => $requestData,
            'response' => $response,
            'http_code' => $this->lastRequestInfo['http_code']
        ];
        
        file_put_contents(
            $this->logFile,
            json_encode($logData, JSON_PRETTY_PRINT) . "\n\n",
            FILE_APPEND
        );
    }
    
    //HTTP методы
    
    public function get($endpoint, $queryParams = []) {
        if (!empty($queryParams)) {
            $endpoint .= '?' . http_build_query($queryParams);
        }
        return $this->request('GET', $endpoint);
    }
    
    public function post($endpoint, $data) {
        return $this->request('POST', $endpoint, $data);
    }
    
    public function put($endpoint, $data) {
        return $this->request('PUT', $endpoint, $data);
    }
    
    public function delete($endpoint) {
        return $this->request('DELETE', $endpoint);
    }
}

// использование ApiClient
try {
    $api = new ApiClient('https://jsonplaceholder.typicode.com');
    $api->addHeader('X-Custom-Header: value');
    
    // GET запрос
    $posts = $api->get('posts', ['userId' => 1, '_limit' => 3]);
    echo "GET Posts:\n";
    print_r($posts);
    
    // POST запрос
    $newPost = $api->post('posts', [
        'title' => 'ApiClient test',
        'body' => 'This is a test post from ApiClient',
        'userId' => 1
    ]);
    echo "\nPOST Result:\n";
    print_r($newPost);
    
    // PUT запрос
    $updatedPost = $api->put('posts/1', [
        'title' => 'Updated title',
        'body' => 'Updated body',
        'userId' => 1
    ]);
    echo "\nPUT Result:\n";
    print_r($updatedPost);
    
    // DELETE запрос
    $deleteResult = $api->delete('posts/1');
    echo "\nDELETE Result:\n";
    print_r($deleteResult);
    
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . " (Code: " . $e->getCode() . ")\n";
}
?>
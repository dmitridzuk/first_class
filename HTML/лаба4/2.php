<?php
$str = 'alb2c3';
$regexp = "/[0-9]+/"; 

$result = preg_replace_callback(
    $regexp,
    function ($matches) {
        return $matches[0]+5;
    },
    $str
);
echo $result;
?>

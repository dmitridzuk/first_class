<?php

$a = [123, 222, 1.33, 545454, 12323, 0.22];
echo array_sum($a) / count($a) . "\n";
echo "\n";

echo array_sum(range(1, 100+1)) . "\n";
echo "\n";

$a = [123, 222, 1.33, 545454, 12323, 0.22];
$b = array_map(fn($value) => sqrt($value), $a);
print_r($b);
echo "\n";

$a = array_combine(range("a", "z"), range(1, 26));
print_r($a);
echo "\n";


$str = '1234567890';
$pairs = str_split($str, 2);
$sum = array_sum(array_map("intval", $pairs)); 
echo $sum;

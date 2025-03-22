<?php

$a = 10;
$b = 3;
echo $a % $b . "\n";
echo "\n";

$div = $a % $b;
$mod = $a / $b;
echo ($mod == 0) ? "Делится: $mod" : "Делится с остатком: $div";
echo "\n";
echo "\n";

$st = pow(2, 10);
echo "$st\n";
$a = sqrt(245);
echo "$a\n";
$array = [4, 2, 5, 19, 13, 0, 10];
$sum = 0;
foreach ($array as $item) {
    $sum += $item;
}
$a = sqrt($sum);
echo "$a\n";
echo "\n";

$a = sqrt(379);
echo round($a) . "\n";
echo round($a, 1) . "\n";
echo round($a, 2) . "\n";
$a = sqrt(587);
$arr = ["floor" => floor($a), "ceil" => ceil($a)];
echo $arr["floor"] . "\n";
echo $arr["ceil"] . "\n";
echo "\n";

$arr = [4, -2, 5, 19, -130, 0, 10];
echo min($arr) . "\n";
echo max($arr) . "\n";
echo random_int(1, 100) . "\n";
$array = [];
foreach (range(0, 9) as $i) {
	array_push($array, random_int(1, 100));
}
print_r($array);
echo "\n";

$a = 12.3;
$b = 213.67;
echo abs($a - $b) . "\n";
echo "\n";

$array = [1, 2, -1, -2, 3, -3];
foreach ($array as &$item) {
    $item = abs($item);
}
print_r($array);
echo "\n";

$a = 134;
$array = [];
foreach (range(1, $a+1) as $i) {
	if ($a % $i == 0) {
		array_push($array, $i);	
	}
}
print_r($array);
echo "\n";

$array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$counter = 0;
$sum_ = 0;
foreach ($array as $item) {
	$counter++;
	$sum_ += $item;
	if ($sum_ > 10) {
		break;
	}
}
echo $sum_ . "\n";
echo $counter . "\n";

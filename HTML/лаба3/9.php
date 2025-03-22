<?php

$array = [];
$a = "";
foreach (range(0, 9) as $i) {
	$a .= "x";
	array_push($array, $a);
}
print_r($array);
echo "\n";

function arrayFill(string $str, int $number) {
	$array = [];
	foreach (range(0, $number-1) as $i) {
		array_push($array, $str);
	}
	return $array;
}
print_r(arrayFill("x", 5));
echo "\n";

$array = [[1, 2, 3], [4, 5], [6]];
$sum = 0;
foreach ($array as $sub_array) {
	foreach ($sub_array as $item) {
		$sum += $item;
	}
}
echo $sum . "\n";
echo "\n";

$array = [];
$a = 1;
foreach (range(0, 2) as $_) {
	$sub_array = [];
	foreach (range(0, 2) as $item) {
		array_push($sub_array, $a);
		$a++;
	}
	array_push($array, $sub_array);
}
print_r($array);
echo "\n";

$array = [2, 5, 3, 9];
$result = $array[0] * $array[1] + $array[2] * $array[3];
echo $result . "\n";
echo "\n";

$user = ["name" => "Dmitry", "surname" => "Greeg.", "patronymic" => "Vyache"];
echo $user["surname"] . " " . $user["name"] . " " . $user["patronymic"] . "\n";
echo "\n";

$date = ["year" => 2025, "month" => 3, "day" => 22];
echo $date["year"] . "-" . $date["month"] . "-" . $date["day"] . "\n";
echo "\n";

$array = ["a", "b", "c", "d", "e"];
echo count($array) . "\n";
echo "\n";

$array = ["a", "b", "c", "d", "e"];
echo $array[count($array)-1] . "\n";
echo $array[count($array)-2] . "\n";

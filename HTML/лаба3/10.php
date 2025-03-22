<?php

function test1(int $a, int $b): bool {
	return $a + $b > 10;
}
echo json_encode(test1(1, 2)) . "\n";
echo json_encode(test1(10, 20)) . "\n";
echo "\n";


function test2(int $a, int $b): bool {
	return $a == $b;
}
echo json_encode(test2(1, 2)) . "\n";
echo json_encode(test2(1, 1)) . "\n";
echo "\n";

$test = 0;
if ($test == 0) echo "верно";
echo "\n";
echo "\n";


$age = 34;
if ($age < 10 || $age > 99) {
	echo "$age < 10 || $age > 99" . "\n";
} else {
	$sum = (int)($age / 10) + $age % 10;
	if ($sum <= 9) {
		echo "Сумма цифр однозначна" . "\n";
	} else {
		echo "Сумма цифр двузначна" . "\n";
	}
}
echo "\n";


$arr = [1, 2, 3];
if (count($arr) == 3) {
	echo $arr[0] + $arr[1] + $arr[2];
}

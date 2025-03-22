<?php

function increaseEnthusiasm(string $str): string {
	return $str . "!";
}

echo increaseEnthusiasm("GD");
echo "\n";


function repeatThreeTimes(string $str): string {
	return $str . $str . $str;
}
echo repeatThreeTimes("GD");
echo "\n";


echo increaseEnthusiasm(repeatThreeTimes("GD"));
echo "\n";


function cut(string $str, int $a = 10): string {
	return substr($str, 0, $a);
}
echo cut("14091240918214") . "\n";
echo "\n";


function print_array($array, int $i = 0) {
	if ($i == count($array)) {
		echo "\n";
		return;
	}
	
	echo $array[$i] . " ";
	print_array($array, $i+1);
}
$array = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print_array($array);
echo "\n";


function sumDigits(int $number): int {
    $sum = 0;
    while ($number != 0) {
        $digit = $number % 10;
        $sum += $digit;
        $number = (int)($number / 10);
    }
    return $sum;
}
$a = 4288109429481;
echo $a . " ";
while (true) {
    $a = sumDigits($a);
    echo $a . " ";

    if ($a <= 9) {
    	break;
    }
}


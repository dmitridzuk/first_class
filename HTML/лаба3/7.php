<?php

function printStringReturnNumber(string $str): int {
	echo $str . "\n";
	return intval(str);
}

$my_num = printStringReturnNumber("1");
echo $my_num;
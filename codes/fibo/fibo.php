#!/usr/bin/php
<?php

function fibo($n)
{
if ($n<=1)
{
	return $n;
}
else
{
	return fibo($n-1) + fibo($n-2);
}
}
$_ARGV=$_SERVER['argv']; 
echo fibo(intval($_ARGV[1])); 
?>


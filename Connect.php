<?php 

$servername = "virtualfarmingcommunity.com";
$dBUsername = "virtuity_Admin";
$dBPassword = "VFCadmin";
$dBName = "virtuity_Accounts";

$conn = mysqli_connect($servername, $dBUsername, $dBPassword, $dBName) or die ('Cannot connect to database.');

echo "Succesfully connected to database!";

?>
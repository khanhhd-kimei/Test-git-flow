<?php

$request = new HttpRequest();
$request->setUrl('https://stg.stockcontrol.jp/v2/allocate/');
$request->setMethod(HTTP_METH_POST);

$request->setHeaders(array(
  'postman-token' => '3abcedbb-062b-01fc-c2d4-dcfe2279f9fa',
  'cache-control' => 'no-cache',
  'x-scs-signature' => 'aaa',
  'x-scs-sitecode' => 'dsoms',
  'content-type' => 'application/json'
));

$request->setBody('{
    "total_request": 1,
    "request": [
        {
            "no": 1,
            "mode": 20,
            "identification_code": "1518488160442",
            "itemize": [
                {
                    "corporation_code": "dscnt",
                    "site_code": "dsoms",
                    "new_identification_code": "",
                    "product_code": "JAN",
                    "cs_code": "JAN",
                    "quantity": 1,
                    "extra_option": {
                    }
                }
            ]
        }
    ]
}');

try {
  $response = $request->send();

  echo $response->getBody();
} catch (HttpException $ex) {
  echo $ex;
}
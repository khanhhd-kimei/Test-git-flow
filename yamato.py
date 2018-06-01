#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os

url = "https://ptwebcollect.jp/test_gateway/cvs2.api"

text = u'りんご'

querystring = {"function_div":"B02","trader_code":"888889760","device_div":"1","order_no":"00003601","goods_name":"029407331289","settle_price":"3829","buyer_name_kanji":"00003601","buyer_name_kana":text.encode('utf-8'),"buyer_tel":"01-1234-1234","buyer_email":"tunn@rubygroupe.jp"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "852c9fe9-4969-59a8-bc91-ce90b6c734d2"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)

text = 'アップルコンピューター'
text_u = u'アップルコンピューター'
print(type(text), len(text))
print(type(text_u), len(text_u))
print(text[0:4])
print(text_u[0:4])

# encoding=utf-8
import requests
import qrm_login_hash
qrm_client_data = {
    "mobile": "13326528030",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d"
}
qrm_client = 'http://115.29.142.212:8020'
qrm_client_s = requests.session()
html_doc = qrm_client_s.get(qrm_client + '/login.html').text
s = qrm_login_hash.get_Hash()
hash = s.get_hash_value(html_doc)
data = s.handle_hash(qrm_client_data, hash)
print(data)
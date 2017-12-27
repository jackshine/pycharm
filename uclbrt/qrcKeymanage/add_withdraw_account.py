import requests
host = 'http://192.168.3.19:13733'
show_url = host + '/api/backend/Bank/show?version=1.0.03'
add_url = host + '/api/backend/Withdraw/add?version=1.0.03'
sid = 'rHBTFEoNtjHYcYFDJMgUfIRfjGDdV9RRf+6n/pi0chZbRfFeebhOHBMPi+8RSMruaOZUXAgLbumdmYHcamVuL8eL3EIvcRLVulsJj0iaplLgPwVBKV/WEWYoOv60eOqgjXocb+bw1t2TBNPABooHzgp7iAX6v6uwiw6sTjHJRh69d0kORmWo4OiJuFMWLgeT4m9wH4x6oJzW2YsUNIFemzeM9F1C2CFeIR2CzeNgi2ktw3Dqknd0p2njb5XIAc4L/Ylsw5RiAljoQAya0kKogjEgE3hVBr6NEzfnnwrowD3mTYktNgvBOT5eZ8E+9ER/FgYSpHCsTINr4wdJY2hfKg=='
data ={
    'sid':sid
}
info =  requests.post(show_url,data=data).json()
for i in info['data']:
    card_data ={
        'sid':sid,
        'owner':'linyouwei',
        'bankNo':i['id']+'1234567890',
        'bankCode':i['id']
    }
    s = requests.post(add_url, data=card_data)
    print(s.text)
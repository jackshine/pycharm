#encoding=utf-8
import requests
import time
#广州-客栈 13326528030
cookies = {
    "mz_UCLBRTUID" : "9cecb07d-4eb0-4551-a7d9-8f69fafcedda",
    "mz_UCLBRTUSSID":"Sngt0nC9nsceKMvIzfYIxVSUUxhrx00oftuIFSBYXsG0zwodl%2BCCqjVERuVsB4PFajaSaRkQXkP6x78tmNwKrYP%2F%2BwrrDM4HmrL2lJFd2DbBacEJKVvwl6VoTJfFl%2FP8iPi5dupO2aa5vbCFKbxPH3a3fXm6ubejxrt5lUP%2B%2Fan6gZCy8q6kWIfA5SuSyf5FCK58rmHE73nt5Ze7J8EkTJUO8sokzdvk3zmffks8turupGJ8HrQ3Lu%2BBYNI1of63FMtwaGetpj%2FKmx%2BrgqKQS7gfiTCvP53T3MDDOXWNW43x4A12P%2FeNCI0WeVG0yHUiHHM%2Fljry%2F6ia5iwCHoKAoQ%3D%3D",
    "mz_UCLBRTUSSPS":"d84dd32310c823ca3fc65714de4687ff06417e7da9f847c203f7a9e8ed90cc60421b97644b1f4b6a30e16a9e5cdad1545eb724a33556e680f1e4e58067e6c813",
    "mz_UCLBRTPSTM":"1510658647",
    "mz_think_language":"zh_cn",
    "mz_room_view_style":"1",
    "master_session_id":"jn7trpc6lulbsna7igb803e007",
    "qrm_community_identity":"P1D3MQVxdpVJLzdY",
    "monitor_count":"70",
    "qrm_think_language":"zh_cn"}
host = "http://115.29.142.212:8020"
url = "/Home/Room/addRooms"
link = host+url
for i in range(200):
    data = {"build":"617",
            "floor":"1469",
            "rooms[0][name]":str(i),
            "rooms[0][num]":str(i),
            "rooms[0][no]":str(i),
            "rooms[0][locktype]":"1",
            "rooms[0][layout]":'{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
            }
    print(data)
    time.sleep(0.5)
    req = requests.post(link,cookies=cookies,data=data)
    print(req.text)

#encoding=utf-8
import requests
cookies_b = {"mz_UCLBRTUID":"9cecb07d-4eb0-4551-a7d9-8f69fafcedda",
           "mz_UCLBRTUSSID":"Sngt0nC9nsceKMvIzfYIxVSUUxhrx00oftuIFSBYXsG0zwodl%2BCCqjVERuVsB4PFajaSaRkQXkP6x78tmNwKrYP%2F%2BwrrDM4HmrL2lJFd2DbBacEJKVvwl6VoTJfFl%2FP8iPi5dupO2aa5vbCFKbxPH3a3fXm6ubejxrt5lUP%2B%2Fan6gZCy8q6kWIfA5SuSyf5FCK58rmHE73nt5Ze7J8EkTJUO8sokzdvk3zmffks8turupGJ8HrQ3Lu%2BBYNI1of63FMtwaGetpj%2FKmx%2BrgqKQS7gfiTCvP53T3MDDOXWNW43x4A12P%2FeNCI0WeVG0yHUiHHM%2Fljry%2F6ia5iwCHoKAoQ%3D%3D",
           "mz_UCLBRTUSSPS":"d84dd32310c823ca3fc65714de4687ff06417e7da9f847c203f7a9e8ed90cc60421b97644b1f4b6a30e16a9e5cdad1545eb724a33556e680f1e4e58067e6c813",
           "mz_UCLBRTPSTM":"1510658647",
           "mz_think_language":"zh_cn",
           "mz_room_view_style":"1",
		   "session_id":"6hefv1gvs52crh2qs015lc25p3",
           "master_session_id":"78egnquk28vsj47aoca27umh11",
           "qrm_community_identity":"pzqo4OAXbZk07Bay",
           "qrm_think_language":"zh_cn",
		   "monitor_count":"244"
		   }
params = {
    "id":(None,"546"),
    "status":(None,"3"),
    "agencyId":(None,"1"),
    "representative":(None,"33323"),
    "hotelSign":(None,"00000"),
    "brandTypeId":(None,"1"),
    "typeSignId":(None,"1"),
    "authorityNote":(None,"22244"),
}
req_b = requests.post("http://115.29.142.212:8021/Bpass/ComAuthority/companyStatus/id/546/userloginID/1623.html",files=params,cookies=cookies_b)
print(req_b.text)


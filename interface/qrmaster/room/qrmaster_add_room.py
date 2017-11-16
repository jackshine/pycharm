#encoding=utf-8
import requests
cookies = {"mz_UCLBRTUID":"0a2c9f6f-61e6-4860-b80b-6565969b6695",
           "mz_UCLBRTUSSID":"ckdGuvD7RCuZi0PU9CQEG4w46BxB1K4j%2FWbBYLyQZORe7QtJXw7C1f4%2FObvLLLWkNsavh4u0rvzTqgsFJ0yj%2FesRvSG7b12VRwpyDae%2FhKTbUCVTBTPao0OlS%2BBlSTB5D59I07%2BlzWsvyqbBHAphFVDz4oJXz0jop3QoG7G6jkEMs7HhCrltoWMYaJq4Hn6NRMQ7Pz1nQkBJSnj88nsGcJd9n2yuvaJ4hxIayJiG1IDuHEZ1exzO8Ctf6X%2FYSf0TRZiKAT9x3B3WlEwyIKCXA7%2BOITkIXkrXhXtRwBXka99PUM9shrehJP6FyWQjz%2F7szipbIcE%2B826FL6gQo0jwiA%3D%3D",
           "mz_UCLBRTUSSPS":"b425a3c2bc4f5045d71b99b6540fcece08abe89b5924e0250bb51737495fd5f62df07ba1ddbe987449f228a9e7cf6699aa2596159210af6b33e5b3097ff313f2",
           "mz_UCLBRTPSTM":"1510414270",
           "mz_think_language":"zh_cn",
           "mz_room_view_style":"1",
           "master_session_id":"tepn3udo51gfhpheef3pissbr3",
           "qrm_community_identity":"P1D3MQVxdpVJLzdY",
           "qrm_think_language":"zh_cn"}
data = {"build":"622",
        "floor":"1472",
        "rooms[0][name]":"11",
        "rooms[0][num]":"11",
        "rooms[0][no]":"11",
        "rooms[0][locktype]":"1",
        "rooms[0][layout]":'{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
        }
print(data)
req = requests.post("http://115.29.142.212:8020/Home/Room/addRooms",cookies=cookies,data=data)
print(req.text)

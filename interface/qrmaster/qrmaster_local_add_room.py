#encoding=utf-8
import requests
cookies = {"mz_UCLBRTUID":"afe71014-c750-46be-8dca-5492bdd3dc12",
           "mz_UCLBRTUSSID":"GXk4YNn%2BlDVNxjxGlNvhrINPh6KI1mrpT0fODJElHG8XrjZI1dX%2F3i5cHDV9X1hhWkOhhVHgN7kf9sj%2B7GwmHTN2WmxQqWJgdlQ5%2BpqXA%2FhtiJQpNXMXEo%2Fih45Mu5W6MG4%2FZD2LOqtcNKH1bFnblZr9YxVAXbhygwcylP5z4FQ1MMQunmVMH5srrlZFQ9h2XBwbXiKjO6GwqJck6cPRIwkzZodUAQuD5uVcgAlBpoBUmJeSSBiPqvT75bluK0lxwNowG2GpWOndg6uj9uFDfR0JN54VsVL4Ee8cU9qVpO9QU0UnJO7wwAqjUBenrJL7Q9SaxDapSjLY3N%2FjiDo0AA%3D%3D",
           "mz_UCLBRTUSSPS":"b18192c7b4c13e61e1995d7cd6ef25f35cab3aed57b2b257e2af1d760a96da38c4adfc6f05c999031f53f15e63a7391920a0c50ce33cdc3d34305a83526842d1",
           "mz_UCLBRTPSTM":"1510652798",
           "mz_think_language":"zh_cn",
           "mz_room_view_style":"1",
           "master_session_id":"uh4fl8ddke7qgo2q8afrfk1hr4",
           "qrm_community_identity":"mOlGLDkKMZAezJpN",
		   "monitor_count":"115",
           "qrm_think_language":"zh_cn"}
host = "http://192.168.3.19:6112"
url = "/Home/Room/addRooms"
link = host+url
for i in range(5):
	data = {"build":"617",
        "floor":"1470",
        "rooms[0][name]":str(i),
        "rooms[0][num]":str(i),
        "rooms[0][no]":str(i),
        "rooms[0][locktype]":"1",
        "rooms[0][layout]":'{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
			}
	print(data)
	req = requests.post(link,cookies=cookies,data=data)
	print(req.text)

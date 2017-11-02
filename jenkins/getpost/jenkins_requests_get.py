#encoding=utf8
import unittest
import json
import requests
class JenkinsGetTestCase(unittest.TestCase):
    def setUp(self):
        self.r = requests.get("http://localhost:8080/api/json?tree=jobs[name]")
    def test_get_all_job_names(self):
        dict_data = json.loads(self.r.text)
        print(dict_data)
        print(dict_data['jobs'][0]['name'])

if __name__ == '__main__':
    unittest.main()

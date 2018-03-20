from selenium import webdriver
import os
    # chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # os.environ["webdriver.chrome.driver"] = chromedriver
    # browser = webdriver.Chrome(chromedriver)
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/Default')
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://115.29.142.212:8010/login.html')
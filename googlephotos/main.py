import requests
import urllib.request
from urllib3.contrib.appengine import AppEngineManager
from  bs4 import  BeautifulSoup

import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

#http.request('GET', 'https://photos.app.goo.gl/WFNxmY6cAnG1tBn3A')



#imgUrl = 'http://photos.app.goo.gl/WFNxmY6cAnG1tBn3A'
imgUrl = requests.get('get','https://photos.app.goo.gl/WFNxmY6cAnG1tBn3A')





soup = BeautifulSoup(imgUrl,'html5lib')

soup.prettify






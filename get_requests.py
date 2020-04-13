import requests
from bs4 import BeautifulSoup


url="http://www.cntour.cn"

response=requests.get(url)
print(response.text)

BeautifulSoup(response.test.'lxml')
data=soup.select()
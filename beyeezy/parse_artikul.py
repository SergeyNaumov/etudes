from bs4 import BeautifulSoup as bs
import requests

url='https://beyeezy.ru/katalog/yeezy-boost-350/adidas-yeezy-boost-350-v2-cmpct-panda/'
page = requests.get(url)
print('status_code:',page.text)
if page.status_code==200:
    content=bs(page.text,'lxml')
    print(content)
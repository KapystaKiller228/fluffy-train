import requests
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189'}
#вот это вот нужно чтобы гугл за бота не считал, как при гуглении с VPN

def response(request):
    request = request.replace(" ", "+")
    page = "https://www.google.com/search?client=opera&q=%s&sourceid=opera&ie=UTF-8&oe=UTF-8" % request
    full_page = requests.get(page, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    return str(soup.findAll('span', {'class': 'DFlfde SwHCTb'})[0].text)

request=input('Print your request(example- 200 eur to rub): ')
print(request.replace('to', '= %s' % (response(request))))

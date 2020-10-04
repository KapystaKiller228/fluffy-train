import requests
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189'}
#вот это вот нужно чтобы гугл за бота не считал, как при VPN

def dollar():
    dollar='https://www.google.com/search?client=opera&q=курс+доллара&sourceid=opera&ie=UTF-8&oe=UTF-8'
    full_page=requests.get(dollar, headers=headers)
    soup=BeautifulSoup(full_page.content, 'html.parser')
    return float(str(soup.findAll('span', {'class': 'DFlfde SwHCTb'})[0].text).replace(',','.'))

def euro():
    oiro='https://www.google.com/search?client=opera&hs=y8K&ei=0WN5X7LUNZH4qwG5or-gCA&q=курс+евро&oq=курс+евро&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIFCAAQsQMyAggAMgQIABBDMgcIABCxAxBDMgIIADIFCAAQsQMyBwgAELEDEEMyBQgAELEDMggIABCxAxCDAToECAAQR1CuwCJY5MUiYJTHImgBcAN4AIABYogBjwKSAQEzmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjygIWboJrsAhUR_CoKHTnRD4QQ4dUDCAw&uact=5'
    full_page=requests.get(oiro, headers=headers)
    soup=BeautifulSoup(full_page.content, 'html.parser')
    return float(str(soup.findAll('span', {'class': 'DFlfde SwHCTb'})[0].text).replace(',','.'))

def funt():
    funt='https://www.google.com/search?client=opera&ei=CWZ5X9SwHOr2qwH186yQDA&q=курс+фунта&oq=курс+фунта&gs_lcp=CgZwc3ktYWIQAxgAMgoIABCxAxBGEIICMgIIADIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOgQIABAKOgcIABCxAxBDOgoIABCxAxCDARBDOggIABCxAxCDAToJCAAQChBGEIICUJ3yc1j6hnRgxI90aAJwA3gAgAFuiAGGB5IBAzMuNpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab'
    full_page = requests.get(funt, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    return float(str(soup.findAll('span', {'class': 'DFlfde SwHCTb'})[0].text).replace(',','.'))

def compare(X,Y):
    if X == 1:
        if Y == 1: return '1 USD = 1 USD'
        if Y == 2: return '1 USD = %s EUR' % (dollar() / euro())
        if Y == 3: return '1 USD = %s GBR' % (dollar() / funt())
        if Y == 4: return '1 USD = %s RUB' % (dollar())

    if X == 2:
        if Y == 1: return '1 EUR = %s USD' % (euro() / dollar())
        if Y == 2: return('1 EUR = 1 EUR')
        if Y == 3: return('1 EUR = %s GBR' % (euro() / funt()))
        if Y == 4: return('1 EUR = %s RUB' % (euro()))

    if X == 3:
        if Y == 1: return('1 GBR = %s USD' % (funt() / dollar()))
        if Y == 2: return('1 GBR = %s EUR' % (funt() / euro()))
        if Y == 3: return('1 GBR = 1 GBR')
        if Y == 4: return('1 GBR = %s RUB' % (funt()))

    if X == 4:
        if Y == 1: return('1 RUB = %s USD' % (dollar()))
        if Y == 2: return('1 RUB = %s EUR' % (euro()))
        if Y == 3: return('1 RUB = 1 GBR' % (funt()))
        if Y == 4: return('1 RUB = 1 RUB')

X,Y=map(int, input('Currency Converter\nX > Y\n1- EUR\n2- USD\n3- GBR\n4- RUB\nPrint what are you want(for example 3 1): ').split())
print(compare(X,Y))
#вводить 4 не рекомендую, иначе захочется свалить из этой страны
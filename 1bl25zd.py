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

def compare(X,Y,value):
    if X == 1:
        if Y == 1: return('%s USD = %s USD' % (value,value))
        if Y == 2: return('%s USD = %s EUR' % (value,value*dollar() / euro()))
        if Y == 3: return('%s USD = %s GBR' % (value,value*dollar() / funt()))
        if Y == 4: return('%s USD = %s RUB' % (value,value*dollar()))

    if X == 2:
        if Y == 1: return('%s EUR = %s USD' % (value,value*euro() / dollar()))
        if Y == 2: return('%s EUR = %s EUR' % (value,value))
        if Y == 3: return('%s EUR = %s GBR' % (value,value*euro() / funt()))
        if Y == 4: return('%s EUR = %s RUB' % (value,value*euro()))

    if X == 3:
        if Y == 1: return('%s GBR = %s USD' % (value,value*funt() / dollar()))
        if Y == 2: return('%s GBR = %s EUR' % (value,value*funt() / euro()))
        if Y == 3: return('%s GBR = %s GBR' % (value,value))
        if Y == 4: return('%s GBR = %s RUB' % (value,value*funt()))

    if X == 4:
        if Y == 1: return('%s RUB = %s USD' % (value, value/dollar()))
        if Y == 2: return('%s RUB = %s EUR' % (value,value/euro()))
        if Y == 3: return('%s RUB = %s GBR' % (value,value/funt()))
        if Y == 4: return('%s RUB = %s RUB' % (value,value))

value,X,Y=map(int, input('Currency Converter\nVALUE*X > Y\n1- USD\n2- EUR\n3- GBR\n4- RUB\nPrint VALUE X Y(for example 300 2 4): ').split())
print(compare(X,Y,value))
#вводить 4 не рекомендую, иначе захочется свалить из этой страны
#https://apilayer.com/

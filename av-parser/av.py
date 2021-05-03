import requests
from bs4 import BeautifulSoup
import json
import re
# import brands


base_url = 'https://cars.av.by/'

carslinks = {} 

finalcars = []

for x in range(1,5):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    r = requests.get(f'https://cars.av.by/filter?brands[0][brand]=1485&price_currency=2&page={x}')

    soup = BeautifulSoup(r.content, 'html.parser')
    carslist = soup.find_all('div', class_='listing-item')

    for item in carslist:

        ''' Find car image '''
        photo = item.find('div', class_='listing-item__photo')
        image = photo.find('img')['data-src']

        ''' Find car title '''
        title = item.find('span', class_='link-text').text

        ''' Find car params '''
        params = item.find('div', class_='listing-item__params').text
        # Miles
        mile_param = re.compile(r"(\d{1}\s\d{3})|(\d{2}\s\d{3})|(\d{3}\s\d{3})")
        miles = mile_param.search(params)
        try:
            fmiles = miles.group()
        except:
            fmiles = ''
        # Year
        year_param = re.compile(r"(\d{4})")
        year =  year_param.search(params)
        try:
            fyear = year.group()
        except:
            fyear = ''
        # Volume
        volume_param = re.compile(r"(\d{1}[.]\d{1})")
        volume = volume_param.search(params)
        try:
            fvolume = volume.group()
        except:
            fvolume = ''
        # Transmision
        transmision_param = re.compile(r"(автомат|механика)")
        transmision = transmision_param.search(params)
        try:
            ftransmision = transmision.group()
        except:
            ftransmision = ''
        # Engine
        engine_param = re.compile(r"(бензин|дизель)")
        engine = engine_param.search(params)
        # print(engine.group())
        try:
            fengine = engine.group()
        except:
            fengine = ''

        ''' Find car link '''
        link = item.find('a', href=True)['href']

        ''' Find car price '''
        price_ru = item.find('div', class_='listing-item__price').text
        price_ru = price_ru.replace('р.', ' ').strip()
        price_ru = price_ru.split()

        try:
            for x in price_ru:
                x = int(x)

            price_ru = price_ru[0] + price_ru[1]
        except:
            price_ru = "error"

        ''' Find car price by usd '''
        price_usd = item.find('div', class_='listing-item__priceusd').text
        price_usd = price_usd.replace('≈', ' ')
        price_usd = price_usd.replace('$', ' ').strip()
        price_usd = price_usd.split()
        
        try:
            for x in price_usd:
                x = int(x)
            price_usd = price_usd[0] + price_usd[1]
        except:
            price_usd = "error"
    
        carslinks = {
            'image': image,
            'title': title,
            'params': params,
            'year': fyear,
            'volume': fvolume,
            'engine': fengine,
            'transmision': ftransmision,
            'miles': fmiles,
            'link': link,
            'price_ru': price_ru,
            'price_usd': price_usd
        }

        finalcars.append(carslinks)

# print(len(finalcars))


cars = "cars.json"
with open(cars, 'w', encoding='utf-8') as json_file:
    json.dump(finalcars, json_file, ensure_ascii = False, indent =4)


print('file dumped')
    


   
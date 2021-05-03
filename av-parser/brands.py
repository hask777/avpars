import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://av.by/'

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

r = requests.get(base_url)

soup = BeautifulSoup(r.content, 'html.parser')
brandlist = soup.find('ul', class_='brandslist')

brands_dict = {}

list_brands = []

for brand in brandlist:
    
    try:
        name = brand.find('span').text
    except:
        name = brand.find('span')

    try:
        cars_count = brand.find('small').text
    except:
        cars_count = brand.find('small')

    print(cars_count)

    brands_dict = {
        'name': name,
        'cars_count': int(cars_count)
    }

    list_brands.append(brands_dict)

    print(list_brands)

barnds = "barnds.json"
with open(barnds, 'w', encoding='utf-8') as json_file:
    json.dump(list_brands, json_file, ensure_ascii = False, indent =4)


print("file dumped")



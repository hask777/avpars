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

lis = soup.find_all('li', class_="brandsitem")
print(lis)

brands_dict = {}
list_brands = []

for item in lis:
    car_name = item.find('span').text
    # print(name)

    cars_count = item.find('small').text
    # print(count)
    if int(cars_count) > 25:
        brands_dict ={
            'name': car_name,
            'cars_count': int(cars_count)
        }

    # print(brands_dict)
        list_brands.append(brands_dict)
print(list_brands)

brands = "brands.json"
with open(brands, 'w', encoding='utf-8') as json_file:
    json.dump(list_brands, json_file, ensure_ascii = False, indent =4)

print('File dumped!!!')

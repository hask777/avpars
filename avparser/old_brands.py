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

    # print(cars_count)

    if int(cars_count) > 25:
        brands_dict = {
            'name': name.lower(),
            'cars_count': int(cars_count)
        }

    list_brands.append(brands_dict)
    # list_brands = list_brands.pop(0)
    

    print(list_brands)

<<<<<<< HEAD
# del list_brands[0]

brands = "brands.json"
with open(brands, 'w', encoding='utf-8') as json_file:
=======
del list_brands[0]

barnds = "old_brands.json"
with open(barnds, 'w', encoding='utf-8') as json_file:
>>>>>>> 3aca936eff1718dfd24ce305ca3440394e373333
    json.dump(list_brands, json_file, ensure_ascii = False, indent =4)


print("file dumped")



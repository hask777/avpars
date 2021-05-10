import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import json
from list import brands_code_list
## Display all the columns of the dataframe
pd.pandas.set_option('display.max_columns',None)

for j in brands_code_list:
    # print(j)
    file_name = f"{j}.json"
    # print(file_name)
    df = pd.read_json(file_name)
    ## print shape of dataset with rows and columns
    # print(df.shape)
    try:
        vol = df['year'].unique()
        # print(vol)
    except:
        vol = ''

    array = []
    dicty = {}
    final = {}
    for car_year in vol:
    #     print(year)
        car_count = df.query( 'year == {}'.format(car_year) ).year.count()

    #     dict[f'{item}'] = count    
        dicty = {
            'car_year': int(car_year),
            'car_count': int(car_count)
        }
        
        array.append(dicty)
    final['cars'] = array

    def get_cars_stat(car):   
        knockOuts = car['car_year']
    #     if type(knockOuts) != int:
    #         knockOuts = 1
        return knockOuts

    list1 = sorted(array, key=get_cars_stat, reverse=True)
    print(list1)

    cars = f"{j}_stat.json"
    with open(cars, 'w', encoding='utf-8') as json_file:
        json.dump(list1, json_file, ensure_ascii = False, indent =4)
        print('STAT file dumped')
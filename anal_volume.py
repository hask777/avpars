import pandas as pd
import numpy as np
import json
from avparser.avlist import brands_code_list
## Display all the columns of the dataframe
pd.pandas.set_option('display.max_columns',None)

for j in brands_code_list:
    print(j)
    try:
        file_name = f"{j}.json"
    except:
        print('error:', file_name)
    # print(file_name)
    try:
        df = pd.read_json(file_name)
    except:
        continue
    ## print shape of dataset with rows and columns
    # print(df.shape)
    try:
        vol = df['volume'].unique()
        # print(vol)
    except:
        vol = ''

    array = []
    dicty = {}
    for car_volume in vol:
    #     print(car_volume)
        car_count = df.query( 'volume == {}'.format(car_volume) ).volume.count()
    #     print(car_count)

        try:
            dicty = {
                'car_volume': float(car_volume),
                'car_count': int(car_count)
            }
        except:
            print('dictionary error')
    
        array.append(dicty)

    def get_cars_stat(car):   
        knockOuts = car['car_volume']

    #     if type(knockOuts) != int:
    #         knockOuts = 1

        return knockOuts

    list1 = sorted(array, key=get_cars_stat, reverse=True)
    print(list1)

    cars = f"{j}_vol_stat.json"
    with open(cars, 'w', encoding='utf-8') as json_file:
        json.dump(list1, json_file, ensure_ascii = False, indent =4)
        print('STAT file dumped')



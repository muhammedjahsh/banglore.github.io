
import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')
__locations =None
__data_columns =None
__model = None

def get_estimated_price(total_sqft,location,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)



def load_save_artifects():
    print('loading saved aritifects ...start')
    global __data_columns
    global __locations

    with open('D:/jahsh data scientist/BHP/server/artifects/columns.json','r') as f:

        __data_columns=json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    

    with open('D:/jahsh data scientist/BHP/server/artifects/banglore_home_prices_model.pickle','rb') as f:
        __model=pickle.load(f)

        
    
    print('loading saved artifects.......done')


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__=='__main__':
    load_save_artifects()
    print(get_location_names())
    print(get_estimated_price(3000,'Yeshwanthpur',2,2))
    # print(get_estimated_price('valarad',2000,3,2))
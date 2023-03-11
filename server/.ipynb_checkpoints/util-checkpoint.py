import json
import pickle
__locations= None
__data_columns= None
__model= None


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved data start....")
    for i in range(1,10):
    	s="====="
    	print(s*i+">"+"    "+str(i*10)+"%")
    	print()
    global __data_columns
    global __locations
    with open('./artifacts/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']   #dictionary
        __locations=__data_columns[3:]
    with open('./artifacts/banglore_home_price_model.pickle','rb') as f:
        __model=pickle.load(f)
    print('Loading data done ... 100 %')

if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    
    
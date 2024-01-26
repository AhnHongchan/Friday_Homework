import requests
import pprint

def get_deposit_products():
    api_key = 'c57884002f9c919c3a616f59c7135007'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }

    response = requests.get(url, params = params).json()
    result_1 = response['result'].keys()
   
    return result_1

if __name__ == '__main__':
    result = get_deposit_products()
    
    pprint.pprint(result)
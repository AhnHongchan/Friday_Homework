import requests
from pprint import pprint as print

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    api_key = 'c57884002f9c919c3a616f59c7135007'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }

    response = requests.get(url, params = params).json()

    optionList = response['result']['optionList']
    baseList = response['result']['baseList']

    
    temp_fin = []

    for one_base in baseList:
        temp_rate = []
        new_dict2 = {}
        new_dict2['금융 상품명'] = one_base['fin_prdt_nm']
        new_dict2['금융 회사명'] = one_base['kor_co_nm']
        base_fin_co = one_base['fin_prdt_cd']
        for one_option in optionList:
            option_fin_co = one_option['fin_prdt_cd']
            if base_fin_co == option_fin_co:
                option_dict = {}
                option_dict['저축 금리'] = one_option['intr_rate']
                option_dict['저축 기간'] = one_option['save_trm']
                option_dict['저축금리유형'] = one_option['intr_rate_type']
                option_dict['저축금리유형명'] = one_option['intr_rate_type_nm']
                option_dict['최고 우대금리'] = one_option['intr_rate2']
                temp_rate.append(option_dict)
        new_dict2['금리 정보'] = temp_rate    
        temp_fin.append(new_dict2)

    return temp_fin

if __name__ == '__main__':
    result = get_deposit_products()
    
    print(result)
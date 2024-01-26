import requests
import pprint

# 전체 정기예금 상품 리스트를 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "baseList" 인 데이터를 출력합니다.


def get_deposit_products():
    api_key = 'c57884002f9c919c3a616f59c7135007'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }

    response = requests.get(url, params = params).json()

    result_2 = response['result']['baseList']
    # len(result_2) = 40
    
    return result_2

if __name__ == '__main__':
    result = get_deposit_products()
    
    pprint.pprint(result)
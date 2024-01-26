# 01pjt



## Problem_1
### API key를 할당받기
 - API key를 할당받는 과정에서 원인 모를 오류 발생
 - 등록 인증이 완료된 뒤에는 문제가 없었음


```import requests
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
    
    pprint.pprint(result)```



## Problem_2
### Key값 출력하기
 - 전체 정기예금의 응답을 json 형태로 변환 후 아래와 같이 Key 값만 출력하도록 구성합니다.
 - ```dict_keys(['prdt_div', 'total_count', 'max_page_no', 'now_page_no', 'err_cd', 'err_msg', 'baseList', 'optionList'])```
 - 공식 문서의 요청 변수 및 예제 요청결과(JSON) 부분을 참고합니다.
 - [힌트] 모든 데이터는 JSON 객체의 "result" 키 값으로 조회할 수 있습니다.
 - response = requests.get(url, params = params).json()
 - if __name__ == '__main__':
 - 위의 두 코드에 대한 추가공부가 필요하다.
 - response['result'].keys()
    - ['result'] : 딕셔너리의 'result' key에 대한 value
    - .keys() : 위의 value값이 딕셔너리이기 때문에 해당 딕셔너리에 대한 key들을 따로 리스트로 담기는 것을 확인할 수 있다.
  - **중첩된 리스트와 딕셔너리의 각 요소**들을 어떤 식으로 출력할 것인지에 대한 고민을 많이 하여야 한다.



```import requests
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
    
    pprint.pprint(result)```



## Problem_3
### key값이 baselist인 데이터 출력하기
 - 1번을 풀고 나서 비교적 쉽게 풀린 문제
 - key에 대한 value를 일일이 [0], [1] 하면서 넣어줬는데 딕셔너리 사이즈를 잘못봐서 벌어진 잘못
 - 딕셔너리와 리스트를 좀 더 잘 살펴볼 것

### Key값이 optionlist인 데이터를 출력하고, 이를 한글화하기
 - new_dict['금융상품코드'] = i['fin_prdt_cd']
 - 새로운 딕셔너리 세트를 만드는 것을 잘 연습할 필요가 있다.
 - 좌변 : 새로운 key / 우변 : result_3 안에 들어간 value
 - 4번 문제에서 지정 문자들을 싹다 갈아엎은 것처럼 result_3, result_4 등과 같은 넘버링과
 for 문에서 문자를 주로 사용함에도 불구하고 i로 지정하는 것과 같은 건 지양하는 것이 좋겠다.
 - 쓰는 단어의 길이가 조금 길어져도 코드를 통으로 봤을 때 헷갈릴 가능성이 매우 줄어듦



```import requests
import pprint

# 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
# 이 때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.

def get_deposit_products():
    api_key = 'c57884002f9c919c3a616f59c7135007'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }

    response = requests.get(url, params = params).json()

    result_3 = response['result']['optionList']
    result_4 =[]
    for i in result_3:
        new_dict = {}
        new_dict['금융상품코드'] = i['fin_prdt_cd']
        new_dict['저축 금리'] = i['intr_rate']
        new_dict['저축 기간'] = i['save_trm']
        new_dict['저축금리유형'] = i['intr_rate_type']
        new_dict['저축금리유형명'] = i['intr_rate_type_nm']
        new_dict['최고 우대금리'] = i['intr_rate2']
        result_4.append(new_dict)

    return result_4

if __name__ == '__main__':
    result = get_deposit_products()```



## Problem_4
### Key값이 baselist, optionlist인 데이터들 중 일부를 뽑아와 원하는 금리 정보 만들기
 - baselist와 optionlist의 공통된 'fin_prdt_cd'를 통해 딕셔너리 안에 딕셔너리를 만드는 과정을 확인하기
 - base_fin_co == option_fin_co 와 같이 둘이 동일하다는 표시를 '=='로 해야하지만 아직도
  '=' 로 쓰는 경향이 있음 : 지금 꼭 고쳐야함
 - 성재의 경우 one_base['fin_prdt_cd'] == one_option['fin_prdt_cd']의 형태로 써서
 내가 개별적으로 base_fin_co, option_fin_co로 지정한 만큼의 길이를 줄이는 역할을 함
 - 코드의 길이를 줄읾과 동시에 가독성을 높이는 방법에 대해서 계속 고민해보기

 - 관통프로젝트는 꼭 복습해볼 것.


```import requests
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
    
    print(result)```
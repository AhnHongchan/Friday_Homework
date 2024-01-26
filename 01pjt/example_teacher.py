# 변수 사용법
# 파이썬

# 서버로부터 데이터를 가져와보세요
# https://fakestoreapi.com/carts

# 서버로부터 데이터 요청 보내야 함
# 실제로 정상적인지 판단
# -> 보안에 위협
# 출력
# 원하는 형태의 데이터 변환

# 라이브러리 : 남들이 만들어놓은 코드를 가져다가 쓰자!
# 데이터를 가져오는 python 라이브러리 : requests
# 파이썬 패키지 관리: pip
    # 설치 : pip install < 패키지이름 >
    # 목록 확인: pip list

# 내 코드에 다른 패키지를 추가

# func()

# 1. 내 파일에서 검색
# 2. 내장모듈 모아둔 곳 검색

import requests
import pprint
# 
api_key = '87246d75e1ce26e1392a087b3d1d88c5'

# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97
# 해당 주소로부터 데이터를 가져와라 / JSON 형태로
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()

pprint.pprint(data)
pprint.pprint(data['weather'])
pprint.pprint(data['weather'][0]['description'])
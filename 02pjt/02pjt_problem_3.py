import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def file_open_by_numpy():
    # np.loadtxt(구분자 = ',', 데이터 타입: string)
    np_arr = np.loadtxt('NFLX.csv', delimiter=",", encoding='cp949', dtype=str)
    return np_arr

arr = file_open_by_numpy()
# print(arr)
df = pd.DataFrame(arr)
# print(df)

# 컬럼명 지정하면서 생성하기
# 인덱스명도 지정하면서 할 수 있다.
columns=arr[0]
arr = np.delete(arr, 0, 0)
df = pd.DataFrame(arr, columns=columns)
# print(df)
# print(df.loc[3])

df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df['Close'] = df['Close'].astype(float)
# Close 타입을 float로 변경
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month

df = df.loc[:, 'Date':'Close']
# Date에서 Close까지만 읽어오기
df['Date'] = pd.to_datetime(df['Date'])
# Date의 형식을 datetime으로 변경
idxs = df[df['Date'] < "2021-01-01"].index
df.drop(idxs, inplace=True)
# 2021년 데이터만 추리는 과정

max_price = df['Close'].max()
min_price = df['Close'].min()
print('최고 종가:', max_price)
print('최저 종가:', min_price)
# 종가의 최대값, 최소값을 구함

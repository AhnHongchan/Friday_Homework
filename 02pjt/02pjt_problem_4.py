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

# max_df = df.max()
# print(max_df)
# 각 항목별 최대값 구하기

df['Y_M'] = df['Date'].dt.strftime("%Y-%m")
# Date의 형식을 연, 월만 나오게 하는 Y_M 형태를 추가
# print(df)

mean_df = df.groupby('Y_M')['Close'].mean()
# 동일한 연-월을 기준으로 그룹화해서 그 때의 종가의 평균값을 구함
# print(mean_df)

mean_df.plot()
plt.title("Monthly Average Close price")
plt.xlabel("Date")
plt.ylabel("Average Close Price")
plt.show()
# 위의 mean_df를 시각화하는 과정

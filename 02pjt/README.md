# PJT 02

## 버전1_금융
데이터 분석과 관련된 내용 진행
실제 분석보다는 주어진 자료를 어떤 식으로 추출하고 분류할껀지에 초점이 맞춰짐

### Problem_1
 - 데이터 중 일부 필드만 읽어오기
 - 무난한 문제
 ```
 df = df.loc[:, 'Date':'Close']
 # Date에서 Close까지만 읽어오기
 ```

### Problem_2
 - 데이터 전처리 : 2021년 이후의 종가 데이터 출력하기
 ```
 df = df.loc[:, 'Date':'Close']
# Date에서 Close까지만 읽어오기
df['Date'] = pd.to_datetime(df['Date'])
# Date의 형식을 datetime으로 변경
idxs = df[df['Date'] < "2021-01-01"].index
df.drop(idxs, inplace=True)
# 2021년 이후의 데이터만 추리는 과정



df.plot('Date', 'Close')
plt.title("NFLX Close Price")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()
# 데이터 전처리 - 2021년 이후의 종가 데이터 출력
```
drop이라는 메서드를 통해 본래 데이터에서 버리는 형태를 만들 수 있었다.

### Problem_3
- 데이터 분석: 2021년 이후 최고, 최저 종가 출력하기
```
max_price = df['Close'].max()
min_price = df['Close'].min()
print('최고 종가:', max_price)
print('최저 종가:', min_price)
# 종가의 최대값, 최소값을 구함
```

- max, min 사용하는 법만 안다면 쉽게 풀 수 있는 문제

### Problem_4
- 데이터 분석: 2021년 이후 월별 평균 종가 출력하기
```
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
```
 - 상당히 애를 먹었던 첫 번째 구간이다.
 - 우선 연-월만 나오게 하는 방식을 몰라서 계속 고민했다.
 - to_datetime을 통해 문자열(object)을 datetime64 타입으로 변경하면 다양한 메서드를 이용할 수 있다.
 - dt.date / dt.year 등
 - 그런데 이 방법으로 답이 안 보이자 다시 찾아보니
 - dt.strftime이라는 것이 있었고 이를 통해 문자열로 바꿔서 년-월만 나오는 형태로 새로운 열을 만들었다.
 - 열을 만든 뒤는 .groupby를 이용해 묶은 뒤 평균을 구했다.

 - dt 내의 다양한 기능을 알아내는 것이 이 문제의 포인트

### Problem_5
```
idxs_2 = df[df['Date'] < "2022-01-01"].index
df.drop(idxs_2, inplace=True)
print(df)

fig, ax = plt.subplots()
ax.plot(df['Date'], df['High'], label = 'High')
ax.plot(df['Date'], df['Low'], label = 'Low')
ax.plot(df['Date'], df['Close'], label = 'Close')
plt.title('High, Low, and Close Prices since January 2022',fontsize=15) 
## 타이틀 설정
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.show()
```

- 이 문제에서 애를 먹은 건 3개의 선을 어떻게 한 그래프 안에 담느냐였다.
- 이를 위해 .subplots()이라는 메서드를 서치했고 이를 활용해 labeling을 하여 완성하였다.
- 3개를 하나를 합친다는 개념 외에는 위와 거의 유사하였다.

## 후기
* 오늘 문제는 생각보다 할만했다.
* 물론 데이터 분석에 관심이 있어서 그런지 집중도가 평소보다 더 올라간 느낌이긴 했다.
* 하지만 여전히 코드 짜는 데 어색한 부분들이 있어서 얼른 실력을 올려야겠다.
# Week 01

## 문제 리스트

|          | 난이도  | 문제제목    | 혼자 풀었나요? |
|----------|------|---------|----------|
| 01/11(목) | Lv01 | 자릿수 더하기 | O        |
<<<<<<< HEAD
| 01/11(목) | Lv01 | 햄버거 만들기 | X        |
| 01/13(토) | Lv02 | 피보나치 수  | O        |
| 01/14(일) | Lv02 | 행렬의 곱셈  | O        |
=======
| 01/11(목) | Lv01 | 햄버거 만들기 | O        |
| 01/13(토) | Lv02 | 피보나치 수  | O        |
>>>>>>> origin/week09/Seonghyeok




## 각 문제풀이별 생각정리
### 1. 문자열 내 p와 y의 개수
X

### 2. 햄버거 만들기
0. 리스트 안에 들어있는 '1231'을 제거
1. 리스트의 맨 앞 부터 4씩 잘라가며 확인
2. 확인 후 맞다면 delete 
3. 리스트에 '1231'이 없을때까지 0~2번 반복
4. 결과 : 66.00/100.00
```angular2html
def solution(ingredient):
    answer = 0
    targetNum = "1231"
    flag = True
    letGrede = []
    
    for i in ingredient:
        letGrede.append(str(i))

    while flag == True:
        # 인덱스가 꼬이게 하지 않기 위해 
        Last = len(letGrede) - 3

        for i in range(Last):
            tmpStr = ''.join(letGrede[i:i + 4])

            if tmpStr == '1231':
                answer += 1
                for _ in range(i, i + 4):
                    del letGrede[i]
            print(letGrede)
        resultStr = ''.join(letGrede)
        if targetNum not in resultStr:
            flag = False

    return answer

```

### 3. 피보나치 수
0. dp로 풀이 진행
<<<<<<< HEAD
1. N = (N-1) + (N-2)


### 4. 행렬의 곱셈
0. arr2의 열 기준으로 다시 정렬
1. 3중 반복문으로 행렬 곱셈 해결
=======
1. N = (N-1) + (N-2)

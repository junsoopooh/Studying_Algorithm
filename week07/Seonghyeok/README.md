# Week 01

## 문제 리스트

|          | 난이도  | 문제제목       | 혼자 풀었나요? |
|----------|------|------------|----------|
| 12/29(금) | Lv01 | 약수의 합      | O        |
| 12/31(일) | Lv01 | 성격 유형 검사하기 | O        |
| 12/31(일) | Lv02 | 최댓값과 최솟값   | O        |
| 12/31(일) | Lv02 | 줄 서는 방법    | O        |





## 각 문제풀이별 생각정리
### 1. 약수의 합
X
### 2. 성격 유형 검사하기


 1. survey를 돌며 하나씩 확인
 1-1. 각 survey의 앞(부정) 뒤(부정)
 2. 각 인덱스의 choices랑 비교하여 점수 선택
 2-1. 선택한 점수에 따라 answer에 알맞은 string join

---> 문제 이해 잘못함 regame

 0. dictionary 초기화
 1. survey를 돌며 하나씩 확인
 1-1. 각 survey의 앞(부정) 뒤(부정)
 2. 각 인덱스의 choices랑 비교하여 점수 선택 하여 알맞은 Dic ++
 3. dic 4번 반복문을 통해 알맞은 답 찾기



### 3. 최댓값과 최솟값
0. 리스트에 int 형태로 값들 넣기
1. max 값 min 값 str로 바꾸어 return

### 4. 줄 서는 방법
0. 라이브러리(permutation)사용하여 결과 찾기
````
from itertools import permutations

def permu(an,k):
    cnt = 0
    for i in permutations(an,len(an)):
        cnt += 1
        if cnt == k:
            return i


def solution(n, k):
    answer = []
    result = []
    for i in range(1,n+1):
        answer.append(i)
    result = permu(answer,k)
    return result
    
    
    
    채점을 시작합니다.
    
    
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (12.97ms, 10.1MB)
테스트 3 〉	통과 (5.57ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.34ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (161.85ms, 10.3MB)
테스트 11 〉	통과 (242.47ms, 10.2MB)
테스트 12 〉	통과 (339.29ms, 10.2MB)
테스트 13 〉	통과 (673.45ms, 10.1MB)
테스트 14 〉	통과 (0.05ms, 10.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
채점 결과
정확성: 73.7
효율성: 0.0
합계: 73.7 / 100.0

````
- 효율성 테스트 실패


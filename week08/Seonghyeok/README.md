# Week 01

## 문제 리스트

|          | 난이도  | 문제제목          | 혼자 풀었나요? |
|----------|------|---------------|----------|
| 12/31(일) | Lv01 | 문자열 내 p와 y의 개수 | O        |
| 01/02(화) | Lv01 | 신규 아이디 추천     | X        |
| 01/03(수) | Lv02 | 최솟값 만들기       | O        |




## 각 문제풀이별 생각정리
### 1. 문자열 내 p와 y의 개수
X
### 2. 신규 아이디 추천
0. 각 단계별로 구현하여 해결
```
from collections import deque

alpha = 'abcdefghijklmnopqrstuvwxyz-_.0123456789'

def solution(new_id):

    new_id = list(new_id)
    removeList = []
    # 1단계 대문자 소문자로 치환
    for i in range(len(new_id)):
    
        if 65 <= ord(new_id[i]) <= 90:
            new_id[i] = chr(ord(new_id[i]) + 32)
            
        if new_id[i] not in alpha:
            removeList.append(new_id[i])
            
    # 2단계 특정 문자열 제외 모든 문자 제거
    if removeList:
        for i in removeList:
            new_id.remove(i)
    # 3단계 연속된 '.' 하나로 치환
    q = deque(new_id)
    dotRemoveList = []
    dotRemoveList.append(q.popleft())
    while q:
        val = q.popleft()
        dotRemoveList.append(val)
        if dotRemoveList[-1] == '.' and dotRemoveList[-1] == dotRemoveList[-2]:
            dotRemoveList.pop()
    # 4 단계
    if dotRemoveList[0] == '.':
        del dotRemoveList[0]
    elif dotRemoveList[-1] == '.':
        del dotRemoveList[-1]
    
    # 5 단계
    if len(dotRemoveList) == 0:
        dotRemoveList.append('a')
    
    resultList = []
    # 6 단계
    if len(dotRemoveList) >= 16:
        resultList = dotRemoveList[:15]
        if resultList[-1] == '.':
            del resultList[-1]
    if len(dotRemoveList) < 16:
        resultList = dotRemoveList
    
    # 7 단계
    if len(resultList) <= 2:
        while 1:
            resultList.append(resultList[-1])
            if len(resultList) == 3:
                break
    # List -> String
    answer = ''.join(resultList)
    
    return answer
```
- 80.8 / 100.0 
- 어디서 문제인지 잘 모르겠다 ..
- 힌트에서 예외 케이스 봄 
- ->".a...b." 일때 "a.b"


### 3. 최솟값 만들기
0. 그리디 문제라고 생각
1. 두 배열을 각각 하나는 오름차순 정렬 하나는 내림차순으로 정렬하여 대응되는 값끼리 곱함
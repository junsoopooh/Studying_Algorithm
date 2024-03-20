## 문제 리스트

|          | 난이도  | 문제제목   | 혼자 풀었나요? |
|----------|------|--------|--------|
| 03/18(월) | Lv01 | 음양 더하기 | O      |
| 03/18(월) | Lv01 | 체육복    | X      |
| 03/19(화) | Lv02 | 캐시     | O      |
| 03/19(화) | Lv02 | 다리를 지나는 트럭     | O      |







## 각 문제풀이별 생각정리
### 1. 하샤드 수
X
### 2. 체육복

<1> 첫 풀이
```
from collections import deque

def solution(n, lost, reserve):
    answer = 0
    reserve = deque(reserve)
    
    while reserve:
        target = reserve.popleft()
        
        if target in lost:
            pass
        else:
            if target-1 in lost:
                lost.remove(target-1)
            elif target+1 in lost:
                lost.remove(target+1)

    answer = n - len(lost)
            
    return answer

```
- 63.3 / 100.0

먼저 정렬을 한 후 진행

<2> 두 번째 풀이
```
from collections import deque

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    reserve = deque(reserve)
    
    while reserve:
        target = reserve.popleft()
        
        if target in lost:
            lost.remove(target)
        else:
            if target-1 in lost:
                lost.remove(target-1)
            elif target+1 in lost:
                lost.remove(target+1)

    answer = n - len(lost)
            
    return answer
```
- 93.3 / 100.0

```angular2html
def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
	
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)
```

### 3. 캐시
1. 제일 큰 분류 cacheSize 대비 현재 queue length
2. 소 분류 --> cache hit or cache miss
3. 추가 고려 사항 :  cities 모두 소문자로 변경

### 4. 다리를 지나는 트럭


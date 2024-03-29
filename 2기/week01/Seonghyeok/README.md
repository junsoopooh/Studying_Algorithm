# Week 01

## 문제 리스트

|          | 난이도  | 문제제목     |혼자 풀었나요?|
|----------|------|----------|-------------|
| 11/10(금) | Lv01 | 평균 구하기   |O|
| 11/13(월) | Lv01 | 신고 결과 받기 |O|
|11/14(화)|Lv02|게임 맵 최단거리|X|



## 각 문제풀이별 생각정리
### 1. 평균 구하기
- 평균 구하는 모듈이나 라이브러리가 있지 않을까 ? 
- 그래서 찾아봄 -> 평균을 구하는 4가지 방법 정리
1. 흔히 아는 반복문으로 구하는 방법
2. 내가 문제에서 푼 **sum**과 **len**을 이용한 평균을 구하는 방법
3. 파이썬 **numpy** 모듈로 평균 구하기
> pip install numpy 모듈을 설치한 후 사용
```
import numpy

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 평균 구하기
average = numpy.mean(arr)

출처: https://blockdmask.tistory.com/559
```
4. statiscics 라이브러리 이용
> 해당 라이브러리는 여러 수학 관련 함수를 제공해줌
> 평균을 구하는 함수는 **mean**이라는 함수
```
import statistics

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [100, 90, 80, 10, 20, 30, 60, 70, 50, 40]

# 평균 구하기
result1 = statistics.mean(arr1)
result2 = statistics.mean(arr2)

출처: https://blockdmask.tistory.com/559 [개발자 지망생:티스토리]
```

### 2. 신고 결과 받기

- 참.. 풀긴 풀었는데 깔끔하게 못푼거같아 아쉬움이 좀 든다.. 
- 다음은 문제를 풀면서 처음부터 들었던 내 생각들


### 한 유저에게 여러번 신고해도 한 번만 신고가 들어감
->  SET 자료형으로 중복 제거 -> 왜? -> 중복을 당할수도 ..  
### k번 이상 신고를 당한 사람을 신고한 사람들에게 발송메일
-> 맞는 해당 인덱스 ++

### dictionary를 사용하면 좋지않을까?
-> report리스트를 dic으로 활용하면 문제를 수월하게 풀어갈수있을거같음<br> -> 튜플로 묶어서 인덱스 늘리는 방향으로 갈려했는데 접근이 안되네

### enumerate를 사용할까?
-> ? 왜
-> 인덱스로 report 리스트에있는 값들 접근하기 위해서

### zip을 사용할까 ?
-> 왜? 값을 묶어주기위해 ..? <br> -> 알게된 사실 : zip 객체는 이터레이션을 통해 소모되면서, 초기화됨


```id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]

report = list(set(report))

k = 3
answer = dict()
for i in id_list:
    answer[i] = 0

# 신고 당한 횟수 저장
for i in range(len(report)):
    tmp = report[i].split(" ")
    answer[tmp[1]] += 1

# 신고당한 횟수가 k 이상인 친구들을 모아두기 위한 리스트
singoList = []

# 신고당한 횟수가 k 이상인 친구들을 찾기 위한 반복문
for key,value in zip(answer.keys(),answer.values()):
    if value >= k:
        singoList.append(key)

# 다시한번 dictionary 초기화 -> 최종적으로 신고했던 친구들의 횟수들을 올리기위해
answer = dict()
for i in id_list:
    answer[i] = 0
    
# singoList를 활용해 신고 횟수가 K이상인 친구들 ++
for i in range(len(report)):
    tmp = report[i].split(" ")
    if tmp[1] in singoList:
        answer[tmp[0]] += 1

# 최종적으로 답을 return 하기위한 List 변환과정
result = []
for i in answer.values():
    result.append(i)
print(result) 
```
### 느낀점
- 파이썬의 자료형과 함수들의 이점을 정확히 파악하고 있지 못하는듯


### 3.게임 맵 최단거리

>    1. 상대 팀 진영에 최소 칸수로 가야한다 -> 최단거리 -> BFS
>    2. 비슷한 문제를 본 것 같다.(이코테 bfs문제 )<br>
>2-1. 숫자 1을 지나가는 좌표를 1씩 더해주면서 최종 목적지에 도착했을때 값 return
>3. 목적지에 도달하지 못할경우도 생긴다.<br>
>3-1. 목적지 (n,m)이라 했을때 둘러싸고있는 (n-1,m) (n,m-1) (n-2,m-2)를 처리 해줘야겠다.<br>
>4. 동,서,남,북 방향 이동은 방향벡터를 사용하자
>5. 행과 열을 나타내는 n과m은 각각 maps의 길이는 '행' maps의 아무 행렬의 길이는 '열'
 
- 위처럼 생각하고 문제를 풀려고했으나 결국 기억이 안나 코드를 다시 봄 But.. 런타임 오류
```
from collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()

    # queue의 시작 0,0
    queue.append((0, 0))
    # 행
    n = len(maps[0])
    # 열
    m = len(maps)
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0 and maps[n-2][m-2] == 0:
        return -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if nx == 0 and ny == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[n - 1][m - 1]

```

- 다른 정답 코드를 보니 상대 팀 진영에 도착하지 못할경우를 잘못생각하여 런타임 오류가 남

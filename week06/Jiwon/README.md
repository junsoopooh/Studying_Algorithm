# Week 06

## 문제 리스트

|                |문제번호|난이도|문제제목|혼자 풀었나요?|
|----------------|-------|------|-------|-------------|
|5/13(토)|10819|하(상)|차이를 최대로|O|
|5/13(토)|10971|하(상)|외판원 순회2|X|
|5/15(월)|14888|중|연산자 끼워넣기|O|
|5/15(월)|1924|하(상)|2007년|O|
|5/17(수)|1182|실버2|부분수열의 합|모의고사|
|5/17(수)|9095|실버3|1, 2, 3 더하기|모의고사|

## 문법, 알고리즘 정리
### dfs 순열
```
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

visited = [False]*N
perm = []

def dfs(m):
    if m == 0:
        print(*perm)
        return
    else:
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                perm.append(i+1)
                dfs(m-1)
                visited[i] = False
                perm.pop()

dfs(M)
```

### dfs 조합
```
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

visited = [False]*N
perm = []

# 중복 반문을 피하기 위해 start 파라미터 이용
# start 파라미터는 현재 노드 이후의 노드 중에서
# 탐색할 첫번째 노드의 인덱스 값!!!
# 이미 방문한 노드들을 모두 방문한 후에 
# 현재 노드에서 이후 노드들을 탐색하게 되어 중복 방문을 피할 수 있음

def dfs(m, start):
    if m == 0:
        print(*perm)
        return
    else:
        for i in range(start, N):
            if visited[i] == False:
                visited[i] = True
                perm.append(i+1)
                dfs(m-1, i+1)
                visited[i] = False
                perm.pop()

dfs(M, 0)
```
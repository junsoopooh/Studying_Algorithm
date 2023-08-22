# 스택 이용한 DFS
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

bigger_lst = [[] for _ in range(N+1)]
smaller_lst = [[] for _ in range(N+1)]
mid = (N+1)/2

for i in range(M):
  a, b = map(int, input().split())
  bigger_lst[b].append(a)
  smaller_lst[a].append(b)

def dfs(arr, start):
  cnt = 0
  visited[start] = True
  stack = deque()
  stack.append(start)
  while stack:
    x = stack.popleft()
    for i in arr[x]:
      if not visited[i]:
        cnt += 1
        visited[i] = True
        stack.append(i)
  return cnt

answer = 0
for i in range(1, N+1):
  visited = [False] * (N+1)
  if dfs(bigger_lst, i) >= mid:
    answer += 1
  if dfs(smaller_lst, i) >= mid:
    answer += 1
print(answer)


# 재귀함수를 이용한 DFS
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

bigger_lst = [[] for _ in range(N+1)]
smaller_lst == [[] for _ in range(N+1)]
mid = (N+1)/2

for i in range(M):
  a, b = map(int, input().split())
  bigger_lst[b].append(a)
  smaller_lst[a].append(b)

def dfs(arr, n):
  global cnt
  for i in arr[n]:
    if not visited[i]:
      visited[i] = True
      cnt += 1
      dfs(arr, i)

answer = 0
for i in range(1, N+1):
  visited = [False] * (N+1)
  cnt = 0
  dfs(bigger_lst, i)
  if cnt >= mid:
    answer += 1
  cnt = 0
  dfs(smaller_lst, i)
  if cnt >= mid:
    answer += 1
print(answer)
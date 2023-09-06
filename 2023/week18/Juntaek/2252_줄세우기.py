# 두 학생의 키를 비교하는 방법을 사용해 오름차순 정렬
# 전부다 비교하는게 아니라 일부만 비교한다.
# 데이터를 받을 때 본인보다 키가 큰 친구들이 본인 인덱스에 담기는 방식으로?

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# answer = []

# for _ in range(M):
#   a, b = map(int, input().split())
#   graph[a].append(b)

# def dfs(start):
#   visited[start] = True
#   for i in graph[start]:
#     if not visited[i]:
#       visited[i] = True
#       answer.append(i)
#       dfs(i)

# for i in range(1, N+1):
#   visited = [False] * (N+1)
#   if not visited[i]:
#     dfs(i)
# print(answer)

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[]  for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
queue = deque()
answer = []

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  inDegree[b] += 1

for i in range(1, n+1):
  if inDegree[i] == 0:
    queue.append(i)

while queue:
  tmp = queue.popleft()
  answer.append(tmp)
  for i in graph[tmp]:
    inDegree[i] -= 1
    if inDegree[i] == 0:
      queue.append(i)

print(*answer)
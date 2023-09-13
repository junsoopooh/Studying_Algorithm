# x로부터 출발하여 도달할 수 있는 도시 찾기
# 최단 거리가 k인 도시 찾기
# 일단 x랑 연결된 도시 bfs 쫙 돌면서 카운트
# 만약 카운트가 k이다? 그러면 그때의 값을 출력하면 되지 않을까?
# 문제는 시작정점과 연결된 정점의 경우 최단거리 1과 최단거리가 아닌 거리와 비교해서 최단거리가 1인 경우엔 출력되면 안됨
# 즉, 만약 최단거리가 1이 아니라면 1과 곧바로 연결된 정점의 경우는 출력되면 안돼.
# 거리를 어떻게 측정해야 되는지 모르겠네.. dfs로 해야하지 않나..?

import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
min_city = []
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
print(graph)

def bfs(start):
  global cnt
  queue = deque()
  queue.append(start)
  while queue:
    cnt = 0
    x = queue.popleft()
    visited[x] = True
    for i in graph[x]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        cnt += 1
        if i not in graph[x] and cnt == k:
          min_city.append(i)

cnt = 0
visited = [False] * (n+1)
bfs(x)
min_city.sort()
if min_city:
  print(min_city)
else:
  print(-1)

# 다른 사람 풀이
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

def bfs(start):
  answer = []
  q = deque([start])
  visited[start] = True
  distance[start] = 0
  while q:
    now = q.popleft()
    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)
        distance[i] = distance[now] + 1
        if distance[i] == k:
          answer.append(i)
  if not answer:
    print(-1)
  else:
    answer.sort()
    for i in answer:
      print(i)

bfs(x)

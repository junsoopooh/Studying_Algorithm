# 모든 도로가 일방통행 도로. 싸이클x
# 사람들이 만나는 시간과 사람들이 지나는 도로의 수를 카운트 하는 프로그램
# n : 도시의 개수
# m : 도로의 개수

# 풀이코드 (https://hiruby.tistory.com/439)
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] * (n+1) for _ in range(n+1)]
back_graph = [[] * (n+1) for _ in range(n+1)]
indegree = [0] * (n+1)
result = [0] * (n+1)
check = [0] * (n+1)
q = deque()
for _ in range(m):
  a, b ,t = map(int, input().split())
  graph[a].append((b, t))
  back_graph[b].append((a, t))
  indegree[b] += 1
start, end = map(int, input().split())

q.append(start)

def topologysort():
  while q:
    cur = q.popleft()
    for i, t in graph[cur]:
      indegree[i]-=1
      result[i] = max(result[i], result[cur] + t)
      if indegree[i] == 0:
        q.append(i)

  cnt = 0
  q.append(end)
  while q:
    cur = q.popleft()
    for i, t in back_graph[cur]:
      if result[cur] - result[i] == t:
        cnt += 1
        if check[i] == 0:
          q.append(i)
          check[i] = 1
  print(result[end])
  print(cnt)

topologysort()

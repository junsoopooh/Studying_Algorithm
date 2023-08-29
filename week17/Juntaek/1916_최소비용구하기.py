# 출발 도시에서 도착 도시까지 가는데 드는 최소 비용 구하기!
# 왜 heap을 써서 가장 거리가 작은 것부터 탐색을 해야하는가?

# import sys
# from collections import deque
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#   s, e, c = map(int, input().split())
#   graph[s].append(e, c)
# start_city, end_city = map(int, input().split())

# def bfs(start):
#   q = deque([start])
#   while q:
#     now = q.popleft()
#     if not visited[now]:
#       for i in graph[now]:
#         if not visited[i]:
#           q.append(i)
#           visited[i] = True

# 풀이 코드
import heapq
from sys import maxsize
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [maxsize] * (n + 1)
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(x):
  pq = []
  heapq.heappush(pq, (0, x))
  visited[x] = 0

  while pq:
    d, x = heapq.heappop(pq)

    if visited[x] < d:
      continue

    for nw, nx in graph[x]:
      nd = d + nw

      if visited[nx] > nd:
        heapq.heappush(pq, (nd, nx))
        visited[nx] = nd
dijkstra(start)
print(visited[end])
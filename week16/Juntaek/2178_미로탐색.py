import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().rstrip())))
print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
        print(graph)
  return graph[n-1][m-1]
print(bfs(0, 0))
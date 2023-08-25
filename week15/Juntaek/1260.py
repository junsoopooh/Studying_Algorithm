import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]

def dfs(x, visited, ans):
  visited[x] = True
  ans.append(x)
  for i in range(1, n+1):
    if not visited[i] and graph[x][i]:
      dfs(i, visited, ans)

def bfs(x, visited, ans):
  visited[x] = True
  options = deque()
  options.append(x)
  while options:
    now = options.popleft()
    ans.append(now)
    for i in range(1, n+1):
      if not visited[i] and graph[now][i]:
        options.append(i)
        visited[i] = True

ans_dfs = []
ans_bfs = []
dfs(v, visited_dfs, ans_dfs)
bfs(v, visited_bfs, ans_bfs)
print(*ans_dfs, sep=' ')
print(*ans_bfs, sep=' ')
import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
cnt = 0
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(start):
    visited[start] = True
    print(visited)
    for i in graph[start]:
      if visited[i] != True:
        dfs(i)

visited = [False for _ in range(n+1)]
print(visited)
for i in range(1, n+1):
  if visited[i] != True:
    cnt += 1
    dfs(i)
print(cnt)
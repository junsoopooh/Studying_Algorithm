import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

def dfs(node):
  global result
  for neighbor in graph[node]:
    if (visited[neighbor] == -1):
      if (visited[node] == 1):
        visited[neighbor] = 2
      if (visited[node] == 2):
        visited[neighbor] = 1
      dfs(neighbor)

    else:
      if (visited[node] == visited[neighbor]):
        result = False
        return

for _ in range(t):
  v, e = map(int, sys.stdin.readline().split())

  visited = [-1] * (v+1)

  graph = [[] for _ in range(v+1)]

  for _ in range(e):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

  result = True

  for i in range(1, v+1):
    if (visited[i] == -1):
      visited[i] = 1
      dfs(i)
      if (result == False):
        break

  if (result == False):
    print('NO')
  else:
    print('YES')

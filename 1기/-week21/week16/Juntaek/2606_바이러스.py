import sys
input = sys.stdin.readline
n = int(input())
v = int(input())
cnt = 0
graph = [[] for _ in range(n+1)]
for _ in range(v):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
  global cnt
  visited[start] = True
  for i in graph[start]:
    if not visited[i]:
      dfs(i)

visited = [False] * (n+1)

# print(visited)
dfs(1)
print(sum(visited) - 1)


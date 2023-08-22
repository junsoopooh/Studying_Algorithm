com_num = int(input())
n = int(input())
graph = [[] for _ in range(com_num+1)]
for _ in range(n):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (com_num+1)
cnt = 0

def dfs(start):
  visited[start] = True
  for i in graph[start]:
    if not visited[i]:
      dfs(i)

dfs(1)
print(sum(visited)-1)
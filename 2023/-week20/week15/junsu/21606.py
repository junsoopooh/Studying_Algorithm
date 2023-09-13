import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(v+1)]
cnt = 0

def dfs(x):
    global cnt
    for i in graph[x]:
        if not visited[i]:
            if arr[i-1] == '1':
                cnt += 1
            else:
                visited[i] = True
                dfs(i)
                visited[i] = False

for s in range(1, n+1):
    if arr[s-1] == '1':
        visited[s] = True
        dfs(s)
        visited[s] = False
print(cnt)

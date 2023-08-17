import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0 for _ in range(n+1)]
def dfs(x):
    for i in graph[x]:
        if not ans[i]:
            ans[i] = x
            dfs(i)

dfs(1)
for i in range(2,n+1):
    print(ans[i])
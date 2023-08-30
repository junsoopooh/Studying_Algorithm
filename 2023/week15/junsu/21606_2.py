import sys
sys.setrecursionlimit(10**6)

def dfs(x,visited,graph,arr):
    cnt = 0
    for i in graph[x]:
        if arr[i-1] == '1':
            cnt += 1
        else:
            if not visited[i]:
                visited[i] = True
                cnt += dfs(i,visited,graph,arr)
    return cnt

n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[0] = True

for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
for i in range(1,n+1):
    if arr[i-1] == '0':
        if not visited[i]:
            visited[i] = True
            tmp = dfs(i, visited, graph, arr)
            ans += tmp*(tmp-1)
    else:
        for j in graph[i]:
            if arr[j-1] == '1':
                ans += 1
print(ans)
import sys
from heapq import heappop, heappush

n,m = map(int,sys.stdin.readline().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = max(graph[a][b],c)
    graph[b][a] = max(graph[b][a],c)
start, arrive = map(int,sys.stdin.readline().split())

def bfs(p,q):
    arr = []
    heappush(arr,(-1e9,p))
    while arr:
        limit,now = heappop(arr)
        limit *= -1
        if now == q:
            return limit
        for i in range(1,n+1):
            if not graph[now][i] or graph[now][i]>limit:
                continue
            tmp = min(limit,graph[now][i])
            heappush(arr,(-1*tmp,i))

ans = bfs(start,arrive)
print(ans)
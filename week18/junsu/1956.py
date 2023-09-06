import sys
from heapq import heappush, heappop
v,e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])

visited = [0 for _ in range(v+1)]
def dfs(now,cnt,start):
    if now == start and cnt:
        return cnt
    for next, cost in graph[now]:
        if not visited[next] or (visited[next] > cost + cnt):
            visited[next] = cost + cnt
            dfs(next,cnt+cost,start)
 
ans = []           
for i in range(1,v+1):
    if dfs(i,0,i):
        ans.append(dfs(i,0,i))
if ans:
    print(min(ans))
else:
    print(-1)
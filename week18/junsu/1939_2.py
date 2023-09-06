import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
start,arrive = map(int,sys.stdin.readline().split())      
    
def bfs(w):
    visited[start] = 1
    arr = deque()
    arr.append(start)
    while arr:
        now = arr.popleft()
        if now == arrive:
            return True
        for next_now, next_limit in graph[now]:
            if not visited[next_now] and next_limit >= w:
                arr.append(next_now)
                visited[next_now] = True
    return False
     
left = 1  
right = 1e9
while left <= right:
    visited = [False for _ in range(n+1)]
    mid = (left+right)//2
    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1
print(int(right))
import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
visited = [ False for _ in range(n+1)]

def bfs(x):
    visited[x] = True
    arr = deque()
    arr.append(x)
    while arr:
        now = arr.popleft()
        for i in range(1,n+1):
            if not visited[i] and graph[now][i] == 1:
                arr.append(i)
                visited[i] = True

bfs(1)
cnt = 0
for i in range(1,n+1):
    if visited[i] == True:
        cnt += 1
print(cnt-1)
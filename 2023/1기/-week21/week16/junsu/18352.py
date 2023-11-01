import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

ans = []
visited = [0 for _ in range(n+1)]

def bfs(s):
    visited[s] = 1
    arr = deque()
    arr.append(s)
    while arr:
        now = arr.popleft()
        for next in graph[now]:
            if not visited[next]:
                arr.append(next)
                visited[next] = visited[now]+1

bfs(x)
ans = []
if k == 0:
    print(x)
else:
    for i in range(1, n+1):
        visited[i] -= 1
        if i == x:
            continue
        if visited[i] == k:
            print(i)
            ans.append(i)
if not ans:
    print(-1)
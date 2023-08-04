import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = graph[v][u] = 1

visited = [False for _ in range(n+1)]
visited[0] = True


def bfs(k, cnt):
    visited[k] = True
    arr = deque()
    arr.append(k)
    while arr:
        now = arr.popleft()
        for i in range(1, n+1):
            if graph[now][i] == 1 and not visited[i]:
                arr.append(i)
                visited[i] = True
        if False not in visited:
            break
    cnt += 1
    return cnt


ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += bfs(i, 0)
print(ans)

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
level = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    level[b] += 1

arr = deque()

for i in range(1, n+1):
    if not level[i]:
        arr.append(i)

ans = []
while arr:
    now = arr.popleft()
    ans.append(now)
    for i in graph[now]:
        level[i] -= 1
        if not level[i]:
            arr.append(i)

print(*ans)

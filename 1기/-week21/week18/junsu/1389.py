import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def cal(s):
    arr = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        arr[i] = search(s, i)
    return sum(arr)


def search(a, b):
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append([a, 0])
    visited[a] = True
    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append([next, cnt+1])


min_val = 1e9
ans = [0]
for i in range(1, n+1):
    tmp = cal(i)
    if tmp < min_val:
        min_val = tmp
        ans[0] = i
    elif tmp == min_val:
        ans.append(i)
print(min(ans))

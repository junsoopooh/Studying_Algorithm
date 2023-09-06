import sys
from heapq import heappop, heappush
v = int(sys.stdin.readline())
tmp = []
for _ in range(v):
    tmp.append(list(map(int, sys.stdin.readline().split())))

graph = [[] for _ in range(v+1)]
for arr in tmp:
    x = 1
    while x < len(arr):
        if arr[x] == -1:
            break
        graph[arr[0]].append([arr[x], arr[x+1]])
        graph[arr[x]].append([arr[0], arr[x+1]])
        x += 2


def bfs(a):
    visited = [0 for _ in range(v+1)]
    q = []
    heappush(q, [0, a])
    while q:
        cnt, now = heappop(q)
        cnt *= -1
        for next in graph[now]:
            if not visited[next[0]] and next[0] != a:
                visited[next[0]] = cnt+next[1]
                heappush(q, [-1*(cnt+next[1]), next[0]])
    return max(visited)


ans = 0
for start in range(1, v+1):
    ans = max(ans, bfs(start))
print(ans)

import sys

n = int(sys.stdin.readline())
graph = [[]]
for _ in range(n):
    graph.append([0] + list(map(int, sys.stdin.readline().split())))

visited = [0 for _ in range(n+1)]
visited[0] = 1


def dfs(s, e, cnt, arr):
    val = []
    if sum(arr) == n+1 and graph[s][e]:
        val.append(cnt + graph[s][e])
        return min(val)
    for i in range(1, n+1):
        if graph[s][i] and not arr[i]:
            arr[i] = 1
            dfs(i, e, cnt+graph[s][i], arr)
            arr[i] = 0

ans = 10**9

for i in range(1, n+1):
    visited[i] = 1
    if dfs(i, i, 0, visited):
        tmp = dfs(i, i, 0, visited)
        ans = min(ans, tmp)
    visited[i] = 0
print(ans)

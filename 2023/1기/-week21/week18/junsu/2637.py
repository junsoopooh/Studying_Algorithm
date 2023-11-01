import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
level = [0 for _ in range(n+1)]
cost = [0 for _ in range(n+1)]
cost[n] = 1
for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append([y, k])
    level[y] += 1

arr = deque()
ans = []
arr.append(n)

while arr:
    now = arr.popleft()
    for i in graph[now]:
        cost[i[0]] += i[1]*cost[now]
        level[i[0]] -= 1
        if not level[i[0]]:
            arr.append(i[0])

for i in range(1, n+1):
    if not graph[i]:
        print(i, cost[i])

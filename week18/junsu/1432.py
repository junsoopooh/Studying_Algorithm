import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
tmp = []
for _ in range(n):
    tmp.append(list(sys.stdin.readline().rstrip()))

graph = [[] for _ in range(n+1)]
level = [0 for _ in range(n+1)]
arr = []
ans = [0 for _ in range(n+1)]
cnt = n

for i in range(n):
    for j in range(n):
        if tmp[i][j] == '1':
            graph[j+1].append(i+1)
            level[i+1] += 1
    if not level[i+1]:
        heappush(arr, -1*(i+1))

while arr:
    now = -1*heappop(arr)
    ans[now] = cnt
    cnt -= 1
    for i in graph[now]:
        level[i] -= 1
        if not level[i]:
            heappush(arr, -1*i)

if 0 in ans[1:]:
    print(-1)
else:
    print(*ans[1:])

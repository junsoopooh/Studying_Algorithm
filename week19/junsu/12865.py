import sys
from heapq import heappush, heappop

n, k = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    if w <= k:
        heappush(arr, [w, v])

n = len(arr)
dp = []
ans = []
dp.append([0, 0])
while arr:
    w, v = heappop(arr)
    for i in range(len(dp)):
        p, q = dp[i]
        if p+w <= k:
            dp.append([p+w, q+v])
            heappush(ans, -1*(q+v))
print(-1*heappop(ans))

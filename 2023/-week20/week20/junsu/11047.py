import sys
from heapq import heappush, heappop

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    heappush(coins, -1*int(sys.stdin.readline()))
cnt = 0
while k > 0 and coins:
    val = -1*coins[0]
    if k >= val:
        tmp = k//val
        cnt += tmp
        k %= val
    heappop(coins)

print(cnt)

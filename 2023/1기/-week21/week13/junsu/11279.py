import sys
from heapq import heappop,heappush
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            tmp = heappop(arr)
        else:
            tmp = 0
        tmp *= -1
        print(tmp)
    else:
        heappush(arr,-x)

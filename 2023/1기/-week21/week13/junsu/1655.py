import sys
from heapq import heappop, heappush, heappushpop
n = int(sys.stdin.readline())
big = []
mid = []
small = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if not mid:
        mid.append(num)
        print(num)
        continue

    if num >= mid:
        tmp = heappushpop(big,num)
        mid.append(tmp)
        print(mid[0])
    else:
        tmp = heappushpop(small,-num)
        mid.append(-tmp)
        mid.sort()
        print(mid[0])
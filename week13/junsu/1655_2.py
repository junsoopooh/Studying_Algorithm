import sys
from heapq import heappop, heappush, heappushpop
n = int(sys.stdin.readline())
large = []
mid = []
small = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if not mid :
        heappush(mid,num)
        print(num)
        continue

    if len(mid) == 2:
        min_val = min(mid)
        if num >= min_val:
            tmp = heappushpop(large,num)

            
        heappush(small,tmp)
        tmp = heappop(mid)
        heappush(large,mid[0])
        mid[0] = tmp
    
    else: 
        heappush(mid,num)
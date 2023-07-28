import sys
from heapq import heappop, heappush, heappushpop
n = int(sys.stdin.readline())
large = []
small = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if not large and not small:
        print(num)
        heappush(large,num)
    elif len(large) == len(small):
        if -small[0] < num:
            heappush(large,num)
            print(large[0])
        else:
            tmp = heappushpop(small,-num)
            heappush(large,-tmp)
            print(large[0])
    else:
        if num >= large[0]:
            tmp = heappop(large)
            heappush(small,-tmp)
            heappush(large,num)
            print(-small[0])
        else:
            heappush(small,-num)
            print(-small[0])
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    number = int(input())

    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))

    else:
        heappush(heap, -number)
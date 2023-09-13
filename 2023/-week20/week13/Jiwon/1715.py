import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

# 최소힙 (오름차순)
heap = []

# 누적 합을 저장할 변수
total = 0

for _ in range(n):
    number = int(input())
    heappush(heap, number)

while True:
    if len(heap) == 1:
        print(total)
        break

    temp = heappop(heap) + heappop(heap)
    heappush(heap, temp)
    total += temp
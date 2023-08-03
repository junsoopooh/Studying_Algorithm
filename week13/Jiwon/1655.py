import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

# left는 최대힙, right은 최소힙
left = []
right = []

for _ in range(n):
    number = int(input())

    if len(left) == len(right):
        heappush(left, -number)
    else:
        heappush(right, number)

    if right and -left[0] > right[0]:
        left_value = heappop(left)
        right_value = heappop(right)
        
        heappush(left, -right_value)
        heappush(right, -left_value)

    print(-left[0])
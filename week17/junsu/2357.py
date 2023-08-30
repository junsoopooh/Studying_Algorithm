import sys
from heapq import heappush, heappop

n, m = map(int, sys.stdin.readline().split())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
arr = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a-1, b-1])


for t in arr:
    start, end = t
    nums_min = []
    nums_max = []
    for i in range(start, end+1):
        number = nums[i]
        heappush(nums_min, number)
        heappush(nums_max, -1*number)
    print(heappop(nums_min), -1*heappop(nums_max), sep=' ')

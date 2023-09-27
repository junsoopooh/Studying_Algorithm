import sys
from heapq import heappop, heappush
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        heappush(arr, list(map(int, sys.stdin.readline().split())))
    k = arr[0][1]
    tmp = []
    for i in arr:
        if i[1] < k:
            heappush(tmp, [i[1], i[0]])
    l = tmp[0][1]
    cnt = 2
    for i in tmp:
        if i[1] < l:
            cnt += 1
    print(cnt)

import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
buildings = []
for _ in range(n):
    l,h,r = map(int,sys.stdin.readline().split())
    buildings.append([l,r,h])

buildings.sort(key=lambda x:x[0])
arr = []
ans = []
for i in buildings:
    if not arr:
        heappush(arr,[-i[2],i[0],i[1]])
        continue
    new_i = [-i[2],i[0],i[1]]
    heappush(arr,new_i)
    while True:
        if arr[0][2] < new_i[1]:
            heappop(arr)
        else:
            break
    if not ans or arr[0][0] != ans[-1]:
        ans.append(arr[0][1])
        ans.append(-arr[0][0])
print(ans)

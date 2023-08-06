import sys
from heapq import heappush, heappop, heappushpop

n = int(sys.stdin.readline())
classes = []
for _ in range(n):
    s,t = map(int,sys.stdin.readline().split())
    classes.append([s,t])

classes.sort()
heap = []
cnt = 1
for i in range(n):
    now_class = classes[i]
    if not heap:
        heappush(heap,now_class[1])
    else:  
        while heap:
            end_time = heap[0]
            if now_class[0] >= end_time:
                heappop(heap)
            else:
                break
        heappush(heap,now_class[1])
    cnt = max(cnt,len(heap))
print(cnt)

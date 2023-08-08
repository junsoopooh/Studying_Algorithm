import sys
from heapq import heappop, heappush

v,e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
dist = [[1e9 for _ in range(v+1)] for _ in range(v+1)]
heap = []
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([c,b])
    dist[a][b] = c
    heappush(heap,[c,a,b])

while heap:
    d,p,q = heappop(heap)
    if p == q:
        print(d)
        break
    
    if dist[p][q] < d:
        continue

    for next_d, next_q in graph[q]:
        new_d = d + next_d
        if new_d < dist[p][next_q]:
            dist[p][next_q] = new_d
            heappush(heap,[new_d,p,next_q])
else:
    print(-1)
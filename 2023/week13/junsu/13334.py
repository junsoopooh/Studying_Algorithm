import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
people = []
for _ in range(n):
    h,o = map(int,sys.stdin.readline().split())
    if h <= o:
        heappush(people,[h,o])
    else:
        heappush(people,[o,h])
d = int(sys.stdin.readline())
ans = 0
while people:
    cnt = 0
    x = people[0][0]
    for person in people:
        if person[0] >= x and person[1] <= x+d:
            cnt += 1
    ans = max(ans,cnt)
    heappop(people)
print(ans)
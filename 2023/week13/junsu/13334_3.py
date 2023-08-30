import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    person = list(map(int, sys.stdin.readline().split()))
    people.append(person)
 
d = int(sys.stdin.readline())
arr = []
for person in people:
    house, office = person
    if abs(house - office) <= d:
        person = sorted(person)
        arr.append(person)
arr.sort(key=lambda x:x[1])

ans = 0
heap = []
for x in arr:
    if not heap:
        heappush(heap, x)
    else:
        while heap[0][0] < x[1] - d:
            heappop(heap)
            if not heap:
                break
        heappush(heap, x)
    ans = max(ans, len(heap))

print(ans)
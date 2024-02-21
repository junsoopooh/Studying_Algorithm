import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
tmp_people = []
people = []
for _ in range(n):
    h,o = map(int,sys.stdin.readline().split())
    if h <= o:
        tmp_people.append([h,o])
    else:
        tmp_people.append([o,h])
d = int(sys.stdin.readline())
for person in tmp_people:
    if person[1]-person[0] <= d:
        people.append(person)
people.sort(key= lambda x:x[1])
ans = 0
k = len(people)
for i in range(k):
    cnt = 0
    x = people[i][0]
    for j in range(i,k):
        if people[j][0] > x+d:
            break
        if people[j][1] <= x+d:
            cnt += 1
    ans = max(ans,cnt)
print(ans)

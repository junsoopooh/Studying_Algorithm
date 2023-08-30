import sys
from collections import deque
r,c = map(int,sys.stdin.readline().split())
forest = []
for _ in range(r):
    forest.append(list(sys.stdin.readline().rstrip()))
animal = deque()
water = deque()
visited = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if forest[i][j] == 'D':
            arrive_a = i
            arrive_b = j
        if forest[i][j] == 'S':
            animal.append([i,j,0])
        if forest[i][j] == '*':
            visited[i][j] = -1
            water.append([i,j])
        if forest[i][j] == 'X':
            visited[i][j] == -2
            
da = [1,0,-1,0]
db = [0,1,0,-1]
now = 0
ans = 'KAKTUS'
while animal:
    a,b,t = animal.popleft()
    if visited[a][b] == -1:
        continue
    if a == arrive_a and b == arrive_b:
        ans = now
        break
    if now != t:
        now = t
        for i in range(4):
            if water:
                water_a, water_b = water.popleft()
                new_water_a = water_a + da[i]
                new_water_b = water_b + db[i]
                if new_water_a < 0 or new_water_a >= r or new_water_b < 0 or new_water_b >= c:
                    continue
                visited[new_water_a][new_water_b] = -1
                water.append([new_water_a,new_water_b])
    for i in range(4):
        na = a + da[i]
        nb = b + db[i]
        if na < 0 or na >= r or nb < 0 or nb >= c:
            continue
        if visited[na][nb] == 0:
            animal.append([na,nb,t+1])
print(ans)
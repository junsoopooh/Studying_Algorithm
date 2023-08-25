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
            
da = [1,0,-1,0]
db = [0,1,0,-1]
now = 0
ans = 'KAKTUS'

def flood(a,b,tmp):
    for i in range(4):
        na = a + da[i]
        nb = b + db[i]
        if na < 0 or na >= r or nb < 0 or nb >= c:
            continue
        if forest[na][nb] != 'X' or forest[na][nb] != 'D':
            visited[na][nb] == tmp + 1
            water.append([na,nb])

def bfs():
    global ans, now
    while animal:
        a,b,t = animal.popleft()
        if a == arrive_a and b == arrive_b:
            ans = t
            break
        
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if na < 0 or na >= r or nb < 0 or nb >= c:
                continue
            if not visited[na][nb] and forest[na][nb] != 'X':
                animal.append([na,nb,t+1])
    return ans
print(bfs())
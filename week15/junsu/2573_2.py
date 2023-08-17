import sys

def check(a, b):
    global n, m
    cnt = 1
    visited = [[False] * m for _ in range(n)]
    visited[a][b] = True
 
    arr = [(a, b)]
 
    while arr:
        a, b = arr.pop()
 
        for dir in range(4):
            na = a + da[dir]
            nb = b + db[dir]
 
            if not visited[na][nb] and graph[na][nb] != 0:
                arr.append((na,nb))
                visited[na][nb] = True
                cnt += 1
 
    return cnt
 
 
n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
melt = [[0] * m for _ in range(n)]
 
da = [-1, 0 , 1, 0]
db = [0, 1, 0, -1]
 
ice = []
for i in range(1, n-1):
    for j in range(1, m-1):
        if graph[i][j] != 0:
            ice.append((i, j))
 
ans = 0
years = 0
while ice:
    if len(ice) != check(ice[0][0], ice[0][1]):
        ans = years
        break
    years += 1
    melt_co = []
    for i in range(len(ice) - 1, -1, -1):
        a, b = ice[i]
 
        for dir in range(4):
            na = a + da[dir]
            nb = b + db[dir]
 
            if graph[na][nb] == 0:
                melt[a][b] += 1
 
        if melt[a][b] > 0:
            melt_co.append((a, b, i))
 
    for a, b, i in melt_co:
        graph[a][b] -= melt[a][b]
        if graph[a][b] <= 0:
            graph[a][b] = 0
            ice.pop(i)
 
        melt[a][b] = 0
 
print(ans)
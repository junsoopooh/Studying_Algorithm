import sys

def check(y, x):
    global N, M
    cnt = 1
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
 
    s = [(y, x)]
 
    while s:
        y, x = s.pop()
 
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
 
            if not visited[ny][nx] and arr[ny][nx] != 0:
                s.append((ny,nx))
                visited[ny][nx] = True
                cnt += 1
 
    return cnt
 
 
N, M = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
melt = [[0] * M for _ in range(N)]
 
dy = [-1, 0 , 1, 0]
dx = [0, 1, 0, -1]
 
ice = []
for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j] != 0:
            ice.append((i, j))
 
ans = 0
cnt = 0
while ice:
    if len(ice) != check(ice[0][0], ice[0][1]):
        ans = cnt
        break
    cnt += 1
    melt_co = []
    for i in range(len(ice) - 1, -1, -1):
        y, x = ice[i]
 
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
 
            if arr[ny][nx] == 0:
                melt[y][x] += 1
 
        if melt[y][x] > 0:
            melt_co.append((y, x, i))
 
    for y, x, i in melt_co:
        arr[y][x] -= melt[y][x]
        if arr[y][x] <= 0:
            arr[y][x] = 0
            ice.pop(i)
 
        melt[y][x] = 0
 
print(ans)
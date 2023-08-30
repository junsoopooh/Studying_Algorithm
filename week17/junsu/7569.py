import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().split())
graph = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    graph.append(tmp)

da = [1, 0, -1, 0, 0, 0]
db = [0, 1, 0, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]
tomato = deque()
cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] != -1:
                cnt += 1
            if graph[i][j][k] == 1:
                tomato.append((i, j, k, 0))
year = 0


def change(x):
    global year
    while tomato:
        c, b, a, y = tomato.popleft()
        print(b)
        for i in range(6):
            nc = c + dc[i]
            nb = b + db[i]
            na = a + db[i]
            if na < 0 or na >= m or nb < 0 or nb >= n or nc < 0 or nc >= h:
                continue
            else:
                if graph[nc][nb][na] == 0:
                    graph[nc][nb][na] = 1
                    tomato.append([nc, nb, na, y+1])
                    year = max(year, y+1)
                    x += 1
    return x


num = change(0)
if num == cnt:
    print(year)
else:
    print(-1)

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
arr = []

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                tomato.append([i, j, k])


def bfs():
    while tomato:
        c, b, a = tomato.popleft()

        for i in range(6):
            nc = c + dc[i]
            nb = b + db[i]
            na = a + da[i]
            if na < 0 or na >= m or nb < 0 or nb >= n or nc < 0 or nc >= h:
                continue
            if graph[nc][nb][na] == 0:
                graph[nc][nb][na] = graph[c][b][a] + 1
                tomato.append([nc, nb, na])


def answer(x):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    x = -1
                    return x
                if graph[i][j][k] > x:
                    x = graph[i][j][k]
    else:
        return x


bfs()
ans = answer(1)
if ans == -1:
    print(ans)
else:
    print(ans-1)

import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
forest = []
for _ in range(r):
    forest.append(list(sys.stdin.readline().rstrip()))
visited = [[0 for _ in range(c)] for _ in range(r)]
arr = deque()
water = deque()
for i in range(r):
    for j in range(c):
        if forest[i][j] == 'S':
            animal_a, animal_b = i, j
            forest[i][j] = '.'
        elif forest[i][j] == '*':
            water.append([i, j])

da = [1, 0, -1, 0]
db = [0, 1, 0, -1]


def flood():
    num = len(water)
    while num:
        a, b = water.popleft()
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if na < 0 or na >= r or nb < 0 or nb >= c:
                continue
            if forest[na][nb] == '.':
                forest[na][nb] = '*'
                water.append([na, nb])
        num -= 1


def bfs(p, q):
    arr.append([p, q])
    visited[p][q] = 1
    while arr:
        num = len(arr)
        while num:
            a, b = arr.popleft()
            for i in range(4):
                na = a + da[i]
                nb = b + db[i]
                if na < 0 or na >= r or nb < 0 or nb >= c:
                    continue
                if visited[na][nb] == 0 and forest[na][nb] == '.':
                    visited[na][nb] = visited[a][b] + 1
                    arr.append([na, nb])
                elif forest[na][nb] == 'D':
                    print(visited[a][b])
                    return
            num -= 1
        flood()
    print('KAKTUS')
    return


flood()
bfs(animal_a, animal_b)

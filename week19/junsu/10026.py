import sys
from collections import deque
n = int(sys.stdin.readline())
board = []
board_d = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    board.append(word)

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board_d[i][j] = 'R'
        else:
            board_d[i][j] = board[i][j]


def bfs(a, b, graph):
    if graph[a][b] == 0:
        return False
    da = [1, 0, -1, 0]
    db = [0, 1, 0, -1]
    arr = deque()

    color = graph[a][b]
    graph[a][b] = 0
    arr.append([a, b])
    while arr:
        p, q = arr.popleft()
        for i in range(4):
            na = p + da[i]
            nb = q + db[i]
            if na < 0 or na >= n or nb < 0 or nb >= n:
                continue
            if graph[na][nb] == color:
                graph[na][nb] = 0
                arr.append([na, nb])
    return True


ans = [0, 0]
for i in range(n):
    for j in range(n):
        if bfs(i, j, board):
            ans[0] += 1

for i in range(n):
    for j in range(n):
        if bfs(i, j, board_d):
            ans[1] += 1

print(*ans)

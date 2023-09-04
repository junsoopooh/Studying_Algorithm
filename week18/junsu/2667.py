import sys
from collections import deque

n = int(sys.stdin.readline())

tmp = []
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
ans = []
for _ in range(n):
    tmp.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(n):
        if tmp[i][j] == '1':
            board[i+1][j+1] = 1
        else:
            board[i+1][j+1] = 0


def find(board):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j]:
                arr = deque()
                arr.append([i, j])
                board[i][j] = 0
                ans.append(check(arr, 0))


def check(l, num):
    da = [0, -1, 0, 1]
    db = [1, 0, -1, 0]
    while l:
        p, q = l.popleft()
        num += 1
        for i in range(4):
            np = p + da[i]
            nq = q + db[i]
            if np < 1 or np > n or nq < 1 or nq > n:
                continue
            if board[np][nq]:
                l.append([np, nq])
                board[np][nq] = 0
    return num


find(board)
ans.sort()
print(len(ans))
print(*ans, sep='\n')

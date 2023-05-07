# N = 4를 가정
# 탐색범위 해당 열, 왼쪽아래오른쪽위 대각선/, 왼쪽위오른쪽아래\
# row = 0, col = 0 : diagonal1[0], diagonal2[3]
# row = 0, col = 1 : diagonal1[1], diagonal2[2]
# row = 0, col = 2 : diagonal1[2], diagonal2[1]
# row = 0, col = 3 : diagonal1[3], diagonal2[0]

# row = 1, col = 0 : diagonal1[1], diagonal2[4]
# row = 1, col = 1 : diagonal1[2], diagonal2[3]
# row = 1, col = 2 : diagonal1[3], diagonal2[2]
# row = 1, col = 3 : diagonal1[4], diagonal2[1]

# 이를 수식화, diagonal1[row + col], diagonal2[row - col + N -1]

import sys
input = sys.stdin.readline

N = int(input())

# N = 8

col = [False] * N
diagonal1 = [False] * (2*N - 1)
diagonal2 = [False] * (2*N - 1)

cnt = 0
def dfs(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for i in range(N):
        if col[i] == False and diagonal1[row+i] == False and diagonal2[row-i+N-1] == False:
            col[i] = diagonal1[row+i] = diagonal2[row-i+N-1] = True
            dfs(row + 1)
            col[i] = diagonal1[row+i] = diagonal2[row-i+N-1] = False

dfs(0)
print(cnt)
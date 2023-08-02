
import sys

n = int(sys.stdin.readline())

board = [[1 for _ in range(n)] for _ in range(n)]
cnt = 0
def dfs(i,n): # i 는 열
    global cnt
    for k in range(n): # k는 행
        if board[k][i] == 1:
            for x in range(n):
                board[k][x] = 0             # 행이 k 인곳 모두 0만들기
                board[x][i] = 0             # 열이 i 인곳 모두 0 만들기
                if k+x < n and 0 <= i-x:         # 대각선 행열의 합이 k+i인곳 모두 0 만들기 
                    board[k+x][i-x] = 0
                if 0 <= k-x and i+x < n:
                    board[k-x][i+x] = 0
            board[k][i] = 1                 # (k,i)는 1
            if i == n-1:
                cnt += 1
                return
    
for i in range(n):
    dfs(i,n)
print(cnt)



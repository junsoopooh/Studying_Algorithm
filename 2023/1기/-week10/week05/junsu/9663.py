import sys

n = int(sys.stdin.readline())

board = [[1 for _ in range(n)] for _ in range(n)]
def search(i,j):
    for i in range(0,n): # i행 0열을 기준으로 한다.
        for j in range(0,n):
            board[j][0] = 0 # 모든 행의 0열은 놓을 수 없음            
        board[i][0] = 1 # i행은 놓았으니 1 유지

        for j in range(1,n): # 0열은 놓는 곳이니 제외해야함
            board[i][j] = 0 # i행의 모든 열은  놓을 수 없음
        board[i][j] = 1
# 현재까지 상황 : i행 0열의 가로 세로 못놓는곳은 0으로 제외시켜주었음. 이제 대각선 생각해야함.
        for a in range(0,n):
            for b in range(0,n):
                if abs(a-b) == i:
                    board[a][b] == 0
        board[i][0] = 1

        tmp = 0
        for k in board:
            tmp += sum(k)
        if tmp == 8:
            ans += 1
    
    print(ans)

search(n,0)





# https://school.programmers.co.kr/learn/courses/30/lessons/120866

# board 범위
# N = len(board)
# row_index : 0~(N-1)
# column_index : 0~(N-1)

# row_top = max(0, row-1)
# row_bottom = min(N-1, row+1)
# column_left = max(0, column-1)
# column_right = min(N-1, column+1) 

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

def solution(board):
    N = len(board)

    def counting(r, c):
        row_top = max(0, r-1)
        row_bottom = min(N-1, r+1)
        column_left = max(0, c-1)
        column_right = min(N-1, c+1)
        for i in range(row_top, row_bottom+1):
            for j in range(column_left, column_right+1):
                board[i][j] += 1

    li_count =[]
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                li_count.append((r,c))
    
    for r, c in li_count:
        counting(r, c)

    cnt = 0
    for li in board:
        cnt += li.count(0)

    return cnt

print(solution(board))

print(board)
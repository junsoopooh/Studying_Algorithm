def delete(board, row_len, col_len):
    will_be_deleted = set()
    cnt = 0
    
    for i in range(row_len - 1):
        for j in range(col_len - 1):
            if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                will_be_deleted.add((i, j))
                will_be_deleted.add((i+1, j))
                will_be_deleted.add((i, j+1))
                will_be_deleted.add((i+1, j+1))

    for r,c in will_be_deleted:
        board[r][c] = 0 
        cnt += 1
    
    return cnt

def drop(board, row_len, col_len):
    for col in range(col_len):
        for row in range(row_len):
            cur = row_len - (row + 1) # 아래부터
            bef_row = cur
            bef_value = board[cur][col]
            if board[cur][col] != 0: # 아래부터 0 이 아닌거는
                cur += 1 # 0 아닌 값을 만날때까지 아래로 내려가면서 
                while cur <= row_len - 1 and board[cur][col] == 0:
                    cur += 1
                
                if cur -1 != bef_row:
                    board[cur-1][col] = bef_value
                    board[bef_row][col] = 0
                
                 

def solution(m, n, board):
    new_board = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_board[i][j] = board[i][j] # 연산가능하게 이차원 리스트로 변형 

    answer = 0
    
    while True:
        deleted = delete(new_board, m, n)
        answer += deleted
        if deleted == 0:
            break 
        
        drop(new_board, m, n)
        
    return answer
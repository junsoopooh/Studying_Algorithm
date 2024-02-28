def solution(board, moves):
    stack = []
    ans = 0
    
    depth = len(board)
    for m in moves:
        for d in range(depth):
            if board[d][m-1] != 0:
                if len(stack) != 0 and stack[-1] == board[d][m-1]:
                    stack.pop()
                    ans += 2 # 제거되는 쌍이 아니라 인형의 개수
                    board[d][m-1] = 0 # 뽑힌 인형은 제거
                    break
                else:
                    stack.append(board[d][m-1])
                    board[d][m-1] = 0 # 뽑힌 인형은 제거
                    break
    
    return ans
                
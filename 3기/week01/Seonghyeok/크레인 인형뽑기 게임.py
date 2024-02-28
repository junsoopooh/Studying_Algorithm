def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                target = board[i][m-1]
                board[i][m-1] = 0
                if len(stack) > 0 and target == stack[-1]:
                    answer += 1
                    stack.pop()
                    break
                else:
                    stack.append(target)
                    break
    return answer*2
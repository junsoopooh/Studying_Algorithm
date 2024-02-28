def solution(board, moves):
    n = len(board)
    stk = []
    answer = 0

    # 열에서 가장 위에 있는 인형을 찾는 함수
    # 찾으면 board에서 0으로 바꾸고 반환
    def first_target(row):
        for i in range(n):
            if board[i][row]:
                result = board[i][row]
                board[i][row] = 0
                break
        else:
            result = False
        return result

    # 인형이 있을 때, 이미 들어있는 인형과 동일하면 제거, 아니면 추가
    for x in moves:
        row = x - 1
        tmp = first_target(row)
        if tmp:
            if stk:
                if stk[-1] == tmp:
                    stk.pop()
                    answer += 2
                    continue
            stk.append(tmp)

    return answer

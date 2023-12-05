# def solution(board):
#     answer = 1234
#     # 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성!
#     # 행마다 처음과 끝 인덱스만 기억하고 있으면 되지 않을까 했는데
#     # 만약에 사이에 0이 존재하면 그건 정사각형이 안되네..
#     n = len(board)
#     print(n)
#     for i in board:
#         print(i)

#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')

#     return answer

def solution(board):
    answer = board[0][0]

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = 1 + min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                answer = max(answer, board[i][j])
    return answer ** 2
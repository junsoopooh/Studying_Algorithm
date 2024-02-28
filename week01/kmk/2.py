"""
크레인 인형뽑기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""

cnt = 0

def solution(board, moves):
    n = len(board)

    stack = []

    def pick(num):
        global cnt
        for i in range(n):
            if board[i][num] != 0:
                if not stack:
                    stack.append(board[i][num])
                else:
                    if stack[-1] == board[i][num]:
                        stack.pop()
                        cnt += 2
                    else:
                        stack.append(board[i][num])
                board[i][num] = 0
                break

    for num in moves:
        pick(num - 1)

    return cnt
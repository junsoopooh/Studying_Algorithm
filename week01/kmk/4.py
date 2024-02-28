"""
프렌즈4블록
https://school.programmers.co.kr/learn/courses/30/lessons/17679
"""
def solution(m, n, board):
    answer, board = 0, [list(ls) for ls in board]

    def check(x, y):
        if 0 <= x + 1 < m and 0 <= y + 1 < n:
            return board[x][y] == board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1]

    def move():
        while 1:
            flag = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] != "." and board[i + 1][j] == ".":
                        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                        flag = 1
            if not flag:
                break
    while True:
        remove, tmp = [], []

        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if check(i, j):
                    remove += [[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]]

        if not remove:
            break

        # 없애기
        for a, b in remove:
            if (a, b) not in tmp:
                tmp.append((a, b))
            board[a][b] = "."

        answer += len(tmp)

        move()

    return answer
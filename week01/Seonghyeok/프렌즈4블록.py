board_col = 0
board_row = 0


def finding(r, c, board):
    global board_col
    global board_row

    same_idx = set()
    if r == board_row - 1: return 0
    if c == board_col - 1: return 0

    if board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1]:
        same_idx.update([(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)])

    # 오른쪽, 아래, 오른쪽아래대각선 중 하나라도 같지 않다면 4개 모이지 x
    else:
        return 0
    return same_idx


def solution(m, n, board):
    answer = 0
    global board_col
    board_col = len(board[0])
    global board_row
    board_row = len(board)
    board = [list(b) for b in board]

    while (1):
        blocks = set()
        for r in range(0, board_row):
            for c in range(0, board_col):
                # 값이 있는 경우
                if board[r][c]:
                    is_four = finding(r, c, board)
                    if is_four:
                        blocks.update(is_four)

        if len(blocks) == 0:
            break
        # 지워야 할 블럭들
        answer += len(blocks)

        # 블럭 지우기
        for b in blocks:
            board[b[0]][b[1]] = ""

        # 블록 내리기
        for i in range(0, board_col):
            for j in range(board_row - 1, 0, -1):
                # 지운 블록인 경우
                if not board[j][i]:
                    start = j - 1
                    value = ""
                    # 위로 올라가면서 지우지 않은 블록 찾기(값, 행 저장)
                    while (start > -1):
                        if board[start][i]:
                            value = board[start][i]
                            break
                        start -= 1
                    # 지우지 않은 블록이 있는 경우, 자리바꾸기
                    if value:
                        board[j][i] = value
                        board[start][i] = ""
                    # 지우지 않은 블록이 없는 경우, 다음 열로 이동
                    else:
                        break

    return answer
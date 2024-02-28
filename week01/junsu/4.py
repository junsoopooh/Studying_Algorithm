def solution(m, n, board):
    answer = 0

    # 시계방향으로 90도 회전하는 함수
    # 따라서 n x m 인 배열이 된다.
    # 블록의 추락도 아래가 아닌 왼쪽으로 발생해야 한다.
    arr = [[] for _ in range(n)]
    for k in range(n):
        for i in range(m - 1, -1, -1):
            arr[k].append(board[i][k])

    # 점을 기준으로 오른쪽, 아래, 오른쪽 아래가 모두 동일한지 확인하는 함수
    def check(a, b):
        result = False
        tmp = arr[a][b]
        if arr[a + 1][b] == tmp and arr[a][b + 1] == tmp and arr[a + 1][b + 1] == tmp:
            result = True
        return result

    # 점을 기준으로 오른쪽, 아래, 오른쪽 아래 4개를 지우는 함수.
    # 지워지는 블록이 다른 곳과 겹칠 경우를 대비하여, 실제 지워진 갯수를 계산하여 반환
    def delete(a, b):
        result = 0
        if arr[a][b] != "0":
            arr[a][b] = "0"
            result += 1
        if arr[a + 1][b] != "0":
            arr[a + 1][b] = "0"
            result += 1
        if arr[a][b + 1] != "0":
            arr[a][b + 1] = "0"
            result += 1
        if arr[a + 1][b + 1] != "0":
            arr[a + 1][b + 1] = "0"
            result += 1
        return result

    # 90도 회전하였기 때문에, 왼쪽으로 블록이 떨어지는 함수 구현
    # 각 행마다, 비어있는 열을 발견할 경우 오른쪽을 탐색하여 떨어질 블록을 찾아 바꿔준다.
    # 한 칸씩 떨어뜨리면, 여러 블록을 떨어뜨리는 경우가 복잡해진다.
    def fall():
        for i in range(n):
            for j in range(m):
                if arr[i][j] == "0":
                    for k in range(j + 1, m):
                        if arr[i][k] != "0":
                            arr[i][j] = arr[i][k]
                            arr[i][k] = "0"
                            break

    # '0'이 아니라는 조건을 추가하지 않으면 무한루프가 실행된다.
    while True:
        delete_list = []
        for i in range(n - 1):
            for j in range(m - 1):
                if arr[i][j] != "0" and check(i, j):
                    delete_list.append([i, j])
        if not delete_list:
            break
        for a, b in delete_list:
            tmp = delete(a, b)
            answer += tmp
        fall()

    return answer

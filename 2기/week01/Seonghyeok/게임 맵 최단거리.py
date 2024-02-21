from collections import deque
'''

'''
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()

    # queue의 시작 0,0
    queue.append((0, 0))
    # 행
    n = len(maps[0])
    # 열
    m = len(maps)
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0 and maps[n-2][m-2] == 0:
        return -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if nx == 0 and ny == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[n - 1][m - 1]


print(solution(maps))













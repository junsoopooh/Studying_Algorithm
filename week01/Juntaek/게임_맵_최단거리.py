# 처음 풀이
from collections import deque
def solution(maps):
    answer = 0
    # maps 배열을 bfs 혹은 dfs로 돌면서 벽이 아닌 부분을 하나씩 탐색
    # 이 과정에서 목표지점에 도달하면 그때의 카운터를 answer에 갱신
    # 여러 루트가 존재할텐데 기존의 answer와 새로운 루트의 카운트를 비교해서 더 작은 카운트를 answer 갱신
    # 나는 bfs로 할거다.
    # 어떻게 했더라...
    n = len(maps)
    m = len(maps[0])
    print(n, m)
    def bfs(x, y):
        global count
        count = 1
        que = deque()
        que.append([x, y])
        while que:
            x, y = que.popleft()
            visited[x][y] = 1
            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if not visited[xx][yy] and maps[xx][yy]:
                    que.append([xx, yy])
                    count += 1
                    # print(count)

                if (xx == (n-1)) and (yy == (m-1)):
                    answer = min(answer, count)
                    print(answer)
                    break


    visited = [[False] * n for _ in range(m)]
    bfs(0, 0)
    return answer

# 다른 사람 풀이
from collections import deque
def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
                if maps[nx][ny] == 0: continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
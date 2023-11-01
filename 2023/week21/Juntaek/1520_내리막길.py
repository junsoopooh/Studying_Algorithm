# 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.
# 상하좌우를 체크해서 현재 높이보다 작은 높이가 있으면 이동가능하게
# 근데 왔던 경로로는 돌아가면 안돼
# 탈출 조건은 어떻게? 만약 주변이 다 방문했거나 자신보다 전부 높이가 높은 지역이라면 탈출
# 일단 무조건 자신보다 작은 높이만을 찾으러 댕겨
# 마지막에 오른쪽 아래 지점까지 도착했음은 어떻게? 마지막 좌표의 값이 있다면 도착했다는 것으로 하고 cnt += 1 하는걸로
# M, N = map(int, input().split())
# map = [list(map(int, input().split())) for _ in range(M)]
# print(map)

# def dfs(x, y):
#   visited[x][y] = True
#   dx = [1, -1, 0, 0]
#   dy = [0, 0, 1, -1]
#   for i in range(4):
#     xx = x + dx
#     yy = y + dy
#     if not visited[xx][yy] and map[xx][yy] < map[x][y]:
#       visited[xx][yy] = True
#       dfs(xx, yy)

#     if visited[N-1][M-1]:
#       cnt += 1
#       break

# visited = [False * M for _ in range(N)]
# dfs(0, 0)
# if
# dfs로 문제를 푼다면 오른쪽 아래에 도달했을 때 경로를 어떻게 셀거냐?
# 조건문 달아서 지속적으로 체크?

import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):

    if x == m - 1 and y == n - 1:
        cnt.append(1)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[x][y] > graph[nx][ny]:
                dfs(nx, ny)


m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = []
dfs(0, 0)
print(len(cnt))
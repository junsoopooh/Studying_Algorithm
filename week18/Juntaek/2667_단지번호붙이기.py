# 1: 집이 있는 곳
# 2: 집이 없는 곳
# 연결된 집은 단지를 정하고 번호 붙이기
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램
# 인접행렬 vs 인접리스트?

# 일단 graph를 탐색하면서 1인 구역만나면 거기서 연결된 부분을 상하좌우 다 탐색해 1인 부분만 계속 탐색하면서 더이상 1인 구역 안만나면 거기서 빠져나와
# dfs든 bfs든 노상관
# n = int(input())
# graph = []
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# for _ in range(n):
#   graph.append(list(map(int, input().rstrip())))
# print(graph)
# def dfs(x, y):
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
#       if not visited[nx][ny]:
#         graph[nx][ny] = 2
#         visited[nx][ny] = 1
#         dfs(nx, ny)

# cnt = 0
# answer = []
# for i in range(n):
#   for j in range(n):
#     visited = [[0] * n for _ in range(n)]
#     if not visited[i][j] and graph[i][j] == 1:
#       dfs(i, j)
#       cnt += 1
#       answer.append(visited.count(1))
# print(cnt, answer)

import sys
input = sys.stdin.readline
n = int(input())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))
# print(graph)
def dfs(x, y):
  visited[x][y] = 1
  count = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
      if not visited[nx][ny]:
        graph[nx][ny] = 2
        count += dfs(nx, ny)
  return count

cnt = 0
answer = []
visited = [[0] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j] and graph[i][j] == 1:
      answer.append(dfs(i, j))
      cnt += 1
print(cnt)
answer.sort()
for i in answer:
  print(i)
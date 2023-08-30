import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
ice = []
melt_list = []

for _ in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
print(graph)

for i in range(n):
  for j in range(m):
    if graph[i][j]:
      ice.append((i, j))
print(ice)

# 1년이 지날 때마다 동서남북으로 0인 칸 개수만큼 빙산의 높이가 줄어든다.
# dfs에 들어오면 한 빙산에 동서남북을 다 탐색해서 0인 지점의 개수를 체크
# 각 빙산마다 녹아야 하는 데이터를 담은 리스트를 추가로 만들어야 함
# dfs를 다 돌았을 때 계산된 빙산의 개수가 만약 처음 빙산의 개수와 같지 않다면 이건 두 덩어리 이상으로 분리되었다는 뜻. 그때 몇년째인지를 출력하면 되는 문제.
# def dfs(x, y, graph):
#   visited[x][y] = True
#   for i in range(n):
#     for j in range(m):
#       if graph[x][y]
#   for ice in graph:
#   dx = [1, 0, -1, 0]
#   dy = [0, 1, 0, -1]
#   for i in range(4):
#     x = x + dx[i]
#     y = y + dy[i]
#     if not graph[x][y]:
#       cnt += 1
#     else:
#   melt_list.append([x, y, cnt])

# bfs 풀이
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 1
  seaList = []

  while q:
    x, y = q.popleft()
    sea = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if not graph[nx][ny]:
          sea += 1
        elif graph[nx][ny] and not visited[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = 1
    if sea > 0:
      seaList.append((x, y, sea))
  for x, y, sea in seaList:
    graph[x][y] = max(0, graph[x][y] - sea)

  return

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
  for j in range(m):
    if graph[i][j]:
      ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
  visited = [[0] * m for _ in range(n)]
  delList = []
  group = 0
  for i, j in ice:
    if graph[i][j] and not visited[i][j]:
      group += bfs(i, j)
    if graph[i][j] == 0:
      delList.append((i, j))
  if group > 1:
    print(year)
    break
  ice = sorted(list(set(ice) - set(delList)))
  year += 1

if group < 2:
  print(0)

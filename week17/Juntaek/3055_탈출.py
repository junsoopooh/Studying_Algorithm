# 비어있는 곳: .
# 물이 차있는 지역: *
# 돌: X
# 비버의 굴: D
# 고슴도치의 위치: S
# 매 분마다 사방으로 이동가능, 물도 비어있는 곳으로 확장
# 물과 고슴도치는 돌을 통과x
# 고슴도치 물인곳 이동불가
# 고슴도치는 물이 찰 예정인 칸도 이동불가
# 물은 비버소굴로 이동불가
# 고슴도치가 비버의 굴로 이동하기 위해 필요한 최소 시간 구하기!
# 요구사항을 데이터로 바라보는 연습

# 고슴도치는 물(찰 예정도 포함), 돌을 피해서 .만 보고 가야한다
# 찰 예정인 칸을 고슴도치가 판단하려면 물이 있는 지역부터 사방을 탐색해야하지 않을까?
# 그럼 물이 있는 지역을 먼저 큐에다가 넣으면 되겠네
# 오케이 그럼 물칸에서 사방 돌면서 .칸을 *이걸로 바꿔버려
# 아아 고슴도치 위치도 그다음에 넣어줘야 하네.
# 이후에 고스도치는 .인 곳에 칸만 탐색해서 이동해
# S 위치를 어떤식으로 이동시켜야할까..

# 처음엔 물 찰 예정인 곳을 고슴도치가 가면 안되니 물 먼저 큐에 넣었는데
# 물이 고슴도치 위치를 덮어버려야 하니까 고슴도치가 먼저 큐에 들어가야하네

# import sys
# from collections import deque
# input = sys.stdin.readline

# r, c = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(r)]
# queue = deque()

# for i in range(r):
#   for j in range(c):
#     if graph[i][j] == '*':
#       queue.append((i, j))

# for i in range(r):
#   for j in range(c):
#     if graph[i][j] == '':
#       queue.append((i, j))

# 풀이코드
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(n)]
distance = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
queue = deque()

def bfs(Dx, Dy):
  while queue:
    x, y = queue.popleft()
    if graph[Dx][Dy] == 'S':
      return distance[Dx][Dy]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
          distance[nx][ny] = distance[x][y] + 1
          queue.append((nx, ny))
        elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
          graph[nx][ny] = '*'
          queue.append((nx, ny))
  return "KAKTUS"

for x in range(n):
  for y in range(m):
    if graph[x][y] == 'S':
      queue.append((x, y))
    elif graph[x][y] == 'D':
      Dx, Dy = x, y

for x in range(n):
  for y in range(m):
    if graph[x][y] == '*':
      queue.append((x, y))

print(bfs(Dx, Dy))
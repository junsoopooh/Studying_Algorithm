# 아무 생각이나 써보자구나.
# 이건 4방이 아니라, 6방이야. 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 보관 후 하루가 지나면 익은 것들 주변 6방이 전염된다.
# 대각선으로는 영향 x
# 1: 익은 토마토, 0: 익지 않은 토마토 -1: 토마토가 없는 칸
# 며칠 지나면 다 익게 되는 걸까?
# 만약 저장될 때부터 모든 토마토가 익어 있다면 0을 출력
# 모두 익지 못하는 상황이면 -1을 출력
# 요구사항을 데이터로 바라보는 연습

# import sys
# input = sys.stdin.readline

# n, m, h = map(int, input().split())
# tomato = [list(map(int, input().split())) for _ in range(m)]

# bfs를 돌면서 현재칸이 1,0,-1 중에 1이다?
# 그럼 육방을 돌면서 0인 부분을 다 찾는다.
# 익은 토마토 주변에 익지 않은 좌표들은 list에 좌표 넣어줘
# 근데 여기서 큐에 넣는 친구를 1,0,-1 다 넣어야 하는가 아니면 1인 친구만 넣어야하는가? 1 주변에 있던 0인 놈은 어차피 하루지나면 1인 애로 변해.
# 그럼 0인 친구도 탐색을 결국 해줘야 하는데..
# 하루가 지나면 다시 bfs를 돌아야 하나?

# 풀이 코드
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()

def bfs():
  while queue:
    z, x, y = queue.popleft()
    for i in range(6):
      nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
      if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
        if graph[nz][nx][ny] == 0:
          graph[nz][nx][ny] = graph[z][x][y] + 1
          queue.append((nz, nx, ny))

for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        queue.append((i, j, k))

bfs()

cannot_complete = False
day = 0
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] ==0:
        cannot_complete = True
      day = max(day, graph[i][j][k])

if cannot_complete:
  print(-1)
else:
  print(day-1)
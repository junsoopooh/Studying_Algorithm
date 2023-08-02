# 벽 또는 자기자신과 부딪히면 게임 종료
# 사과를 먹으면 뱀 길이가 늘어남
# N*N 정사각 보드위에서 진행
# 게임 시작시 뱀의 길이는 1
# 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동한다.

from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
  a, b = map(int, input().split())
  graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
  x, c = input().split()
  dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
  global direction
  if alpha == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4

while True:
  cnt += 1
  x += dx[direction]
  y += dy[direction]

  if x < 0 or x >= n or y < 0 or y >= n:
    break

  if graph[x][y] == 2:
    graph[x][y] = 1
    queue.append((x, y))
    if cnt in dirDict:
      turn(dirDict[cnt])

  elif graph[x][y] == 0:
    graph[x][y] = 1
    queue.append((x, y))
    tx, ty = queue.popleft()
    graph[tx][ty] = 0
    if cnt in dirDict:
      turn(dirDict[cnt])

  else:
    break

print(cnt)


### 다른 풀이 ###
from collections import deque

n - int(input())
board = [([0] * n) for _ in range(n)]
apple = []
k = int(input())
for _ in range(k):
  input_row, input_col = map(int, input().split())
  apple_row, apple_col = input_row-1, input_col-1
  board[apple_row][apple_col] = 1
  apple.append((apple_row, apple_col))

L = int(input())
change_snake = []
for _ in range(L):
  dis, direct = input().split()
  dis = int(dis)
  change_snake.append((dis, direct))

change_snake.append((10001, ''))

change = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_snake(direction):
  global turn_index
  if direction == 'L':
    if turn_index != 0:
      turn_index -= 1
    else:
      turn_index = 3
  else:
    if turn_index != 3:
      turn_index += 1
    else:
      turn_index = 0
  return

snake = deque()
snake.append((0, 0))

turn_index = 1
x, y = 0, 0
cnt = 0
start = 1
breaker = False

for i in range(len(change_snake)):
  start = cnt + 1
  for _ in range(start, change_snake[i][0] + 1):
    nx = x + change[turn_index][0]
    ny = y + change[turn_index][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
      cnt += 1
      breaker = True
      break
    if board[nx][ny] == 1:
      board[nx][ny] = 0
      x, y = nx, ny
      snake.append((x, y))
    else:
      x, y = nx, ny
      snake.popleft()
      snake.append((x, y))
    cnt += 1
  if breaker == True:
    break
  turn_snake(change_snake[i][1])
print(cnt)
# 동서남북으로 계속 체크하면서 1인 방 찾아.
# 1인방 큐에다 넣어놓고 하나씩 다시 체크
# 근데 더이상 갈수가 없다? 그러면 흰방을 검은방으로 바꿔야 하는 데..
# 어떤 방을 바꿀지를 어떻게 판단해?

# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().rstrip())) for _ in range(n)]
# print(graph)

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs(x, y, arr):
#   q = deque([(x, y)])
#   while q:
#     now_x, now_y = q.popleft()
#     for _ in range(4):
#       nx = now_x + dx
#       ny = now_y + dy
#       if not visited[nx][ny] and graph[nx][ny]:
#         q.append((nx, ny))
#         visited[nx][ny] = True


# 풀이 코드
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

arr = []
for i in range(N):
  arr.append(list(map(int, input().rstrip())))

def bfs():
  q = deque()
  q.append((0, 0))
  visited = [[-1] * N for _ in range(N)]
  visited[0][0] = 0
  while q:
    x, y = q.popleft()
    if x == N-1 and y == N-1:
      return visited[x][y]
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
        if arr[nx][ny] == 1:
          q.appendleft((nx, ny))
          visited[nx][ny] = visited[x][y]
        else:
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
print(bfs())
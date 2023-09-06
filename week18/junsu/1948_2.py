import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
arr = deque()
level = [0 for _ in range(n+1)]
board = [0 for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append([b, t])
    level[b] += 1

start, arrive = map(int, sys.stdin.readline().split())
arr.append(start)

while arr:
    now = arr.popleft()
    for next in graph[now]:
        next_place = next[0]
        next_time = next[1]
        level[next_place] -= 1
        if board[next_place] < board[now] + next_time:
            board[next_place] = board[now] + next_time
            back_graph[next_place] = [now]
        elif board[next_place] == board[now] + next_time:
            back_graph[next_place].append(now)

        if not level[next_place]:
            arr.append(next_place)

arr = deque()
arr.append(arrive)
route = set()
while arr:
    now = arr.popleft()
    for x in back_graph[now]:
        if (now, x) not in route:
            route.add((now, x))
            arr.append(x)

print(board[arrive])
print(len(route))

import sys
from collections import deque

t = 0
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
snake = deque()
snake.append([1, 1])
apples = []

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    apples.append([a, b])

l = int(sys.stdin.readline())
move = deque()
for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    move.append([x, c])

i = 0
direction_a = [0, -1, 0, 1]
direction_b = [1, 0, -1, 0]

next_move = move.popleft()

while True:
    t += 1
    head_a = snake[-1][0]
    head_b = snake[-1][1]
    head_a += direction_a[i]
    head_b += direction_b[i]
    head = [head_a, head_b]

    if head_a > n or head_a < 1 or head_b < 1 or head_b > n or head in snake:
        break

    snake.append(head)
    if head in apples:
        apples.remove(head)
    else:
        snake.popleft()

    if str(t) == next_move[0]:
        if next_move[1] == 'L':
            i += 1
        else:
            i -= 1
        if move:
            next_move = move.popleft()
        if i > 3:
            i %= i
        elif i < 0:
            i += 4

print(t)

import sys
from collections import deque

t = 0
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
snake = deque()
snake.append([1,1])
apples = []

for _ in range(k):
    a,b = map(int,sys.stdin.readline().split())
    apples.append([a,b])

l = int(sys.stdin.readline())
move = deque()
for _ in range(l):
    x,c = sys.stdin.readline().rstrip().split()
    move.append([x,c])

i = 0
direction_a = [0,-1,0,1]
direction_b = [1,0,-1,0]

next_move = move.popleft()

while True:
    t += 1
    head_a = snake[-1][0]
    head_b = snake[-1][1]
    newhead_a = head_a + direction_a[i]
    newhead_b = head_b + direction_b[i]
    newhead = [newhead_a,newhead_b]
    
    if newhead_a > n or newhead_a < 0 or newhead_b < 0 or newhead_b > n or newhead in snake:
        break
    
    snake.append(newhead)
    if newhead in apples:
        apples.remove(newhead)
    else:
        snake.popleft()
    
    if str(t) == next_move[0]:
        if next_move[1] == 'L':
            i += 1
        else:
            i -= 1
        next_move = move.popleft()
        if i > 3:
            i %= i
        elif i < 0:
            i += 4
    
print(t)
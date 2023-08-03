import sys
from collections import deque
input = sys.stdin.readline

# 보드의 크기
n = int(input())

# 사과의 개수
k = int(input())

# 사과의 위치 (행, 열)
apples = [list(map(int, input().split())) for _ in range(k)]

# 뱀의 방향 변환 횟수
l = int(input())

# 뱀의 방향 변환 정보 (초, 왼/오)
bam = deque([list(map(str, input().split())) for _ in range(l)])

row = 1
column = 1

timer = 0
snake = deque([[row, column]])

# 방향 (right/down/left/up)
direction = 'right'

while True:
    timer += 1

    # 방향 확인
    if len(bam) > 0 and timer == int(bam[0][0]) + 1:
        if bam[0][1] == 'L':
            if direction == 'right': direction = 'up'
            elif direction == 'up': direction = 'left'
            elif direction == 'left': direction = 'down'
            elif direction == 'down': direction = 'right'

        else:
            if direction == 'right': direction = 'down'
            elif direction == 'up': direction = 'right'
            elif direction == 'left': direction = 'up'
            elif direction == 'down': direction = 'left'

        bam.popleft()
    
    if direction == 'right': column += 1
    elif direction == 'up': row -= 1
    elif direction == 'left': column -= 1
    elif direction == 'down': row += 1

    # 벽에 닿으면 게임 종료
    if row == 0 or column == 0 or row == n+1 or column == n+1:
        break

    # 몸에 닿으면 게임 종료
    if [row, column] in snake:
        break

    snake.append([row, column])
    
    if [row, column] in apples:
        # 사과가 있으면 해당 사과 삭제
        apples.remove([row, column])
    else:
        # 사과가 없으면 왼쪽 꼬리 삭제
        snake.popleft()

print(timer)
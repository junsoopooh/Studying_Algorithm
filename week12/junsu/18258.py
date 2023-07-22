import sys
from collections import deque
n = int(sys.stdin.readline())
arr = deque()
for _ in range(n):
    order = list(sys.stdin.readline().rstrip().split())
    if order[0] == 'push':
        arr.append(order[1])
    elif order[0] == 'pop':
        if not arr:
            print(-1)
        else:
            num = arr.popleft()
            print(num)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if not arr:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not arr:
            print(-1)
        else:
            print(arr[0])
    elif order[0] == 'back':
        if not arr:
            print(-1)
        else:
            print(arr[-1])
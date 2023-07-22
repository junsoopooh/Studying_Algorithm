import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque(range(n, 0, -1))
while len(arr) > 1:
    arr.pop()
    num = arr.pop()
    arr.appendleft(num)
print(*arr)

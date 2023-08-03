import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

stack = deque([i+1 for i in range(n)])

print("<", end='')

while len(stack) > 1:
    for i in range(k-1):
        stack.append(stack.popleft())

    print(stack.popleft(), end=', ')

print(f'{stack[0]}>')
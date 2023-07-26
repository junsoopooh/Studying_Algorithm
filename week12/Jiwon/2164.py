import sys
from collections import deque
input = sys.stdin.readline

number = int(input())

values = deque()

for i in range(number):
    values.append(i+1)

while len(values) > 1:
    values.popleft()

    if len(values) == 1:
        break

    values.append(values.popleft())

print(*values)
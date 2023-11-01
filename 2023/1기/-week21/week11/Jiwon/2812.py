import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = list(map(int, input().strip()))

length = k
stack = []

for i in range(n):
    while stack and length > 0 and stack[-1] < values[i]:
        stack.pop()
        length -= 1

    stack.append(values[i])

print(*stack[:n-k], sep='')
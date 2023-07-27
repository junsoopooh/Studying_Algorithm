import sys
input = sys.stdin.readline

# 탑의 수
n = int(input())
values = list(map(int, input().split()))

# 높이, 위치(인덱스+1)
stack = []
result = [0] * n

for i in range(n):
    while stack:
        if stack[-1][0] < values[i]:
            stack.pop()
        else:
            result[i] = stack[-1][1] + 1
            break

    stack.append([values[i], i])

print(*result)
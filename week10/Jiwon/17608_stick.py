import sys
input = sys.stdin.readline

# 막대기 개수
n = int(input())

values = [int(input()) for _ in range(n)]
values = values[::-1]

result = []

for i in range(n):
    if i == 0:
        result.append(values[i])
    else:
        if values[i] > result[-1]:
            result.append(values[i])

print(len(result))
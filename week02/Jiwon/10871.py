import sys
input = sys.stdin.readline

# 수열 A의 개수 n개, x보다 작은 수 출력
n, x = map(int, input().split())
values = list(map(int, input().split()))

for value in values:
    if value < x:
        print(value, end=' ')
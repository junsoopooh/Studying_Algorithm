import sys
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    # 반복 횟수, 값
    count, value = map(str, input().split())

    values = list(value)

    for value in values:
        print(value * int(count), end='')

    print()
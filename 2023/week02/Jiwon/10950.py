import sys
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(a+b)
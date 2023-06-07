import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def solve(a, b, c):
    # 지수가 1이면,
    if b == 1:
        return a % c
    else:
        # 지수가 짝수면,
        if b % 2 == 0:
            return solve(a, b//2, c) ** 2 % c
        # 지수가 홀수면,
        else:
            return solve(a, b//2, c) ** 2 * a % c

print(solve(a, b, c))
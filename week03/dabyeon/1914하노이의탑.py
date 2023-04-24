# 시작기둥 a, 중간기둥 6-a-b, 목표기둥 b

def recursion(n, a, b):
    # 탈출 조건
    if n == 0:
        return
    
    recursion(n-1, a, 6-a-b)
    print(a, b)
    recursion(n-1, 6-a-b, b)

import sys
input = sys.stdin.readline

N = int(input().rstrip())

if N > 20:
    # 최소 이동 횟수는 2^n-1
    print(2**N-1)
else:
    print(2**N-1)
    recursion(N, 1, 3)
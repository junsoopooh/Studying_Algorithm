import sys
input = sys.stdin.readline

N = int(input().rstrip())

for i in range(1, 10):
    print(f'{N} * {i} = {N*i}')
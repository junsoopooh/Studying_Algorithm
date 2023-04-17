import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    A, B = map(int, input().rstrip().split())
    print(A+B)
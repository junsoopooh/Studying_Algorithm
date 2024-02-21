import sys

t = int(sys.stdin.readline())

def combination(a, b):
    tmp_u = tmp_d = 1
    for i in range(a):
        tmp_u *= (b-i)
    for j in range(1, a+1):
        tmp_d *= j
    return tmp_u/tmp_d

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    ans = combination(n, m)
    print(int(ans))
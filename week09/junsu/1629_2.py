import sys

a, b, c = map(int, sys.stdin.readline().split())
sys.setrecursionlimit = 10**9

def solve(a, b, c):
    if b == 1:
        return(a%c)
    else:
        tmp = solve(a, b//2, c)
    if b % 2 == 1:
        return tmp*tmp*a%c
    else:
        return tmp*tmp%c

ans = solve(a, b, c)
print(ans)

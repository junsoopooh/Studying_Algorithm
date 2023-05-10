import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

def solve(n, a, b):
    if n == 0:
        return 0
    else:
        return (2 * (a%2) + (b%2)) + (4 * solve(n-1, (a//2), (b//2)))
    
print(solve(n, a, b))
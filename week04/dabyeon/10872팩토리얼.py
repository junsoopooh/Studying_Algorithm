# factorial n! = n*(n-1)*(n-2)*...*1
# f(n) = f(n-1) * f(n-2)

import sys
input = sys.stdin.readline

N = int(input().rstrip())

def recursion(n):
    if n < 1:
        return 1
    return n * recursion(n-1)

print(recursion(N))
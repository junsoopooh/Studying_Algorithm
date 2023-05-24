import sys

def S(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return S(x-1) + S(x-2) + S(x-3)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    ans = S(n)
    print(ans)




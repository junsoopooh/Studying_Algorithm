import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

perm = []

def dfs(n):
    if n == 0:
        print(*perm)
        return
    else:
        for i in range(N):
                perm.append(i+1)
                dfs(n-1)
                perm.pop()

dfs(M)
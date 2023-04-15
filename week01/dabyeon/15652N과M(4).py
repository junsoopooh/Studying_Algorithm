import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

comb = []

def dfs(start, m):
    if m == 0:
        print(*comb)
        return
    else:
        for i in range(start, N):
            comb.append(i+1)
            dfs(i, m-1)
            comb.pop()

dfs(0, M)
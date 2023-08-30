import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

arr = [i for i in range(n+1)]


def dfs(x, tmp):
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(x,n+1):
        tmp.append(i)
        dfs(i,tmp)
        tmp.pop()
    

for i in range(1, n+1):
    tmp = []
    tmp.append(i)
    dfs(i, tmp)
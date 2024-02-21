import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

visited = [False]*N
perm = []

def dfs(m):
    if m == 0:
        print(*perm)
        return
    else:
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                perm.append(i+1)
                dfs(m-1)
                visited[i] = False
                perm.pop()

dfs(M)
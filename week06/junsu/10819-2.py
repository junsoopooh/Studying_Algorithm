import sys

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
visited = [False]*n
arr = []

def dfs(x):
    if 0 <= x < n:
        for i in range(n):
            if visited[i] == False:
                arr[x] = data[i]
                visited[i] = True
                dfs(x+1)
                visited[i] = False
                arr[x] = 0
    else:
        False

tmp = []
tmp.append(dfs(0))
print(max(tmp))
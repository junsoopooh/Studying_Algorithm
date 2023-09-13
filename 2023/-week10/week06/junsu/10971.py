import sys

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))

visited = [False]*n


def dfs(now,end,cnt):
    visited[now] = True
    visited[end] = True
    if visited.count(False) == 0:
        return cnt
    for next in range(n):
        if visited[next] != True and matrix[now][next] != 0:
            cnt += matrix[now][next]
            visited[next] = True
            dfs(next,end,cnt)
            cnt -= matrix[now][next]
            visited[next] = False
    else:
        False

ans = 10**6
for now in range(n):
    for end in range(n):
        cnt = 0
        if matrix[now][end] and matrix[end][now] and dfs(now,end,cnt):
            tmp = dfs(now,end,cnt) + matrix[end][now]
            ans = min(ans,tmp)
print(ans)


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
num_list = list(map(int, input().rstrip().split()))

num_list.sort()

visited = [False]*N

result = []

def dfs(m):
    if m == 0:
        print(*result)
        return
    else:
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                result.append(num_list[i])
                dfs(m-1)
                visited[i] = False
                result.pop()

dfs(M)
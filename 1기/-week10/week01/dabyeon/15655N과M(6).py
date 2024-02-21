import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
num_list = list(map(int, input().rstrip().split()))

num_list.sort()
visited = [False]*N
comb = []

def dfs(start, m):
    if m == 0:
        print(*comb)
        return
    else:
        for i in range(start, N):
            if visited[i] == False:
                visited[i] = True
                comb.append(num_list[i])
                dfs(i+1, m-1)
                visited[i] = False
                comb.pop()

dfs(0, M)
import sys
sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline())

def dfs(x):
    global ans
    tmp = visited[x]
    for i in graph[x]:
        if not visited[i]:
            if tmp == 1:
                visited[i] = 2
            else:
                visited[i] = 1
            dfs(i)
        else:
            if visited[i] == tmp:
                ans = 'NO'
                return

for _ in range(k):
    ans = 'YES'
    v,e = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0 for _ in range(v+1)]

    for i in range(1, v+1):
        if not visited[i]:
            visited[i] = 1
            dfs(i)
            if ans == 'NO':
                break
    print(ans)
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    graph.append(tmp)
    
dx = [0,-1,0,1]
dy = [1,0,-1,0]
def bfs(n,m):
    arr = deque()
    arr.append([0,0])
    while arr:
        x,y = arr.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= m-1 and graph[nx][ny] == '1':
                arr.append([nx,ny])
                graph[nx][ny] = int(graph[x][y]) + 1
                if nx == n-1 and ny == m-1:
                    return
bfs(n,m)
print(graph[n-1][m-1])
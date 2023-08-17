import sys

v,e = map(int,sys.stdin.readline().split())
graph = [[0 * v] for _ in range(v)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

visited = [False * v]

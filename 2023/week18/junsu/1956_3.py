import sys

v, e = map(int, sys.stdin.readline().split())
graph = [[1e9 for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c


def main():
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    ans = 1e9
    for i in range(1, v+1):
        ans = min(ans, graph[i][i])
    if ans == 1e9:
        print(-1)
    else:
        print(ans)


main()

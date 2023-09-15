import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(1 << n)] for _ in range(n)]


def search(s, visit):
    if visit == (1 << n) - 1:
        if graph[s][0]:
            return graph[s][0]
        else:
            return 1e9

    if dp[s][visit]:
        return dp[s][visit]

    tmp = 1e9
    for i in range(1, n):
        if visit & (1 << i) == 0 and graph[s][i]:
            tmp = min(search(i, visit | (1 << i)) + graph[s][i], tmp)
    dp[s][visit] = tmp
    return dp[s][visit]


print(search(0, 1 << 0))

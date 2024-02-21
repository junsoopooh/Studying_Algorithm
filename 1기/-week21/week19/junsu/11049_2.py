import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        if i == 1:
            dp[j][j+i] = arr[j][0] * arr[j][1] * arr[j+i][1]
            continue

        dp[j][j+i] = 2**32
        for x in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][x] + dp[x+1]
                             [j+i] + arr[j][0] * arr[x][1] * arr[j+i][1])

print(dp[0][n-1])

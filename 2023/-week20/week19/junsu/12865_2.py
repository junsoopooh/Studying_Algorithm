import sys

n, k = map(int, sys.stdin.readline().split())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = arr[i]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value+dp[i-1][j-weight], dp[i-1][j])

print(dp[-1][-1])

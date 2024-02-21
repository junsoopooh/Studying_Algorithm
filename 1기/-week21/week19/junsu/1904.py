import sys

n = int(sys.stdin.readline())
sys.setrecursionlimit(10**9)
dp = [0 for _ in range(n+1)]
for x in range(1, n+1):
    if x == 1:
        dp[x] = 1
    elif x == 2:
        dp[x] = 2
    elif x == 3:
        dp[x] = 3
    else:
        dp[x] = (dp[x-1] + dp[x-2]) % 15746

print(dp[n])

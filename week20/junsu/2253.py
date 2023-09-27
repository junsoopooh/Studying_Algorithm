import sys

n, m = map(int, sys.stdin.readline().split())
x = []
for _ in range(m):
    x.append(int(sys.stdin.readline()))

limit = int(((8*n+1)**0.5-1)//2)+1

dp = [[1e9 for _ in range(limit+1)] for _ in range(n+1)]
dp[1][0] = 0
for i in range(2,n+1):
    if i in x:
        continue
    for jump in range(1,limit+1):
        dp[i][jump] = min(dp[i-jump][jump-1],dp[i-jump][jump],dp[i-jump][jump+1])+1

if min(dp[n]) != 1e9:
    print(min(dp[n]))
else:
    print(-1)

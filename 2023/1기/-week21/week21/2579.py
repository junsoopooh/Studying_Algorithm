import sys

n = int(sys.stdin.readline())
arr = [0]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
    
dp = [[0,0,0] for _ in range(n+1)]

for i in range(1,n+1):
    if i == 1:
        dp[i][1] = arr[1]
        dp[i][2] = 0
    elif i == 2:
        dp[i][1] = arr[2]
        dp[i][2] = arr[1] + arr[2]
    else:
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + arr[i]
        dp[i][2] = dp[i-1][1] + arr[i]

ans = max(dp[n])
print(ans)
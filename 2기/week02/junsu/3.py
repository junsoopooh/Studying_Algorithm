# 2 x n 타일링

def solution(n):
    dp = [0 for _ in range(60001)]
    x = 1
    while x <= n:
        if x == 1:
            dp[x] = 1
        elif x == 2:
            dp[x] = 2
        else:
            dp[x] = (dp[x-1] + dp[x-2])%1000000007
        x += 1 
    return dp[n]
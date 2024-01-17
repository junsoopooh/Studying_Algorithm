# 피보나치 수

def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    if n<2:
        return dp[n]
    for i in range(2,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%1234567
    return dp[n]

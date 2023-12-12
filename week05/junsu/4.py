# 멀리 뛰기

def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = (dp[i-1] + dp[i-2])%1234567
    answer = dp[n]
    return answer

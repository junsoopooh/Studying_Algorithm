def solution(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1] % 1234567
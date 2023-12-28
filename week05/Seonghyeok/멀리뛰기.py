def solution(n):
    dp = [0] * 2000
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    if n == 1:
        return 1

    for i in range(3, n + 2):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[i - 1] % 1234567



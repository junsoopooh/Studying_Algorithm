# 정확성 Only
def solution(n):
    if n <= 3:
        dp = [0, 1, 1, 2]
        return dp[n]
    dp = []
    for i in range(n + 1):
        dp.append(i)
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        k = i // 2
        if i % 2:
            for j in range(k, i):
                dp[i] = min(dp[i], dp[j] + i - j)
        else:
            dp[i] = min(dp[i], dp[k])
            for j in range(k + 1, i):
                dp[i] = min(dp[i], dp[j] + i - j)
    return dp[n]


# 1차 개선
def solution2(n):
    while True:
        if not n % 2:
            n //= 2
        else:
            break
    if n <= 3:
        dp = [0, 1, 1, 2]
        return dp[n]
    dp = []
    for i in range(n + 1):
        dp.append(i)
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        k = i // 2
        if i % 2:
            for j in range(k, i):
                dp[i] = min(dp[i], dp[j] + i - j)
        else:
            dp[i] = min(dp[i], dp[k])
            for j in range(k + 1, i):
                dp[i] = min(dp[i], dp[j] + i - j)
    return dp[n]


# 2차 개선
def solution3(n):
    while True:
        if not n % 2:
            n //= 2
        else:
            break
    if n <= 3:
        dp = [0, 1, 1, 2]
        return dp[n]
    dp = []
    for i in range(n + 1):
        dp.append(i)
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        if i % 2:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i // 2]
    return dp[n]


# 최종
def solution(n):
    cnt = 0
    while n > 3:
        if not n % 2:
            n //= 2
        else:
            cnt += 1
            n -= 1
    if n <= 3:
        dp = [0, 1, 1, 2]
        return dp[n] + cnt

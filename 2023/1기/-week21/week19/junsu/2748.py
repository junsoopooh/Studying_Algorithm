import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
dp[1] = 1


def fibo(x):
    if x == 0:
        return dp[0]
    elif x == 1:
        return dp[1]
    else:
        if dp[x]:
            return dp[x]
        else:
            dp[x] = fibo(x-1) + fibo(x-2)
            return dp[x]


print(fibo(n))

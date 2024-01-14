# 피보나치 함수

import sys

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]


def fibo(x):
    if dp[x] != [0, 0]:
        return dp[x]
    dp[x][0] = fibo(x-1)[0] + fibo(x-2)[0]
    dp[x][1] = fibo(x-1)[1] + fibo(x-2)[1]


for i in range(1, 41):
    fibo(i)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n][0], dp[n][1])

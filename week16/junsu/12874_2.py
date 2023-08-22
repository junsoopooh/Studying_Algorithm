import sys

s = list(sys.stdin.readline().rstrip())
n = len(s)

dp = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
open = 0
tmp = s[0]
i = -1


def fun(x, open):
    next_open_x = next_close_x = 0
    i = x
    while not next_close_x and next_open_x:
        i += 1
        if i == '(' and not next_open_x:
            next_open_x = i
        elif i == ')' and not next_close_x:
            next_close_x = i

    dp[x][open] = dp[next_open_x][open+1] + dp[next_close_x][open-1]

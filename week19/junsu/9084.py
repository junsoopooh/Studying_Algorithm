import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for i in range(1,m+1):
        if i <= coins[0]:
            continue
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                dp[i] += dp[i-coins[j]]        
    print(dp[m])
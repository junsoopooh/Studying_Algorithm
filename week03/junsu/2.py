# 3 x n 타일링 문제
def solution(n):
    dp = [0 for _ in range(5001)]
    dp[2] = 3
    dp[4] = 11
    for i in range(1,n+1):
        if n%2:
            return 0
        
        if i%2:
            continue
        else:
            if not dp[i]:
                tmp = 2
                tmp += dp[i-2]*dp[2]
                for x in range(2,i//2):
                    tmp += dp[i-2*x]*2
                dp[i] = tmp%1000000007
    return dp[n]
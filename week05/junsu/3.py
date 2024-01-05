# 땅따먹기

def solution(land):
    n = len(land)
    answer = 0
    dp = [[0 for _ in range(4)] for _ in range(n)]
    dp[0] = land[0]
    
    def check(next_row,next_col):
        arr = []
        for i in range(4):
            if i == next_col:
                continue
            arr.append(dp[next_row-1][i])
        return max(arr)

    x = 1
    while x < n:
        for i in range(4):
            dp[x][i] = check(x,i) + land[x][i]
        x += 1
    answer = max(dp[-1])
    return answer

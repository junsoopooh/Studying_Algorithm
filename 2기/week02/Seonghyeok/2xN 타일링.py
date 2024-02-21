def solution(n):
    '''
    1. dp배열 생성 및 초기화
    2. 점화식을 토대로 값 배열에 넣기
    '''
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007

    return dp[-1]
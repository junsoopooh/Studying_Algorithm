# 가장 큰 정사각형 찾기

# 내 풀이(효율성 탈락)
def solution(board):
    answer = 1
    p = len(board)
    q = len(board[0])
    if p == 1 or q == 1:
        return answer
    
    def check(a,b):
        cnt = 1
        while True:
            if a+cnt >= p or b+cnt >= q:
                break
            for i in range(a,a+cnt+1):
                for j in range(b,b+cnt+1):
                    if not board[i][j]:
                        return (cnt)**2
            cnt += 1
        return (cnt)**2
    
    for i in range(p):
        for j in range(q):
            if not board[i][j]:
                continue
            tmp = check(i,j)
            if tmp:
                answer = max(answer, tmp)
    return answer
  
# 정답 풀이
def solution(board):
    answer = 0
    p = len(board)
    q = len(board[0])
    dp = [[0 for _ in range(q)] for _ in range(p)]
    dp[0] = board[0]
    for i in range(p):
        dp[i][0] = board[i][0]

    for a in range(p):
        for b in range(q):
            if a-1>=0 and b-1>=0 and board[a][b]==1:
                dp[a][b] = min(dp[a-1][b-1],dp[a-1][b],dp[a][b-1])+1
                answer = max(answer,dp[a][b])
    for i in range(p):
        tmp = max(dp[i])
        answer = max(answer,tmp)
    return answer*answer

# 이해 안되는 부분
# 최솟값 에 1 더하여 dp값을 결정한 후 그떄마다 최솟값을 비교하면 안돼나? 아래처럼?
answer = max(answer,dp[a][b]) 

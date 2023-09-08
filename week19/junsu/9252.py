import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

a = len(A)
b = len(B)

dp = [['' for _ in range(b)] for _ in range(a)]

for i in range(a):
    dp[i][0] = B[0]
    if B[0] == A[i]:
        dp[i][0] = B[0]
    else:
        dp[i][0] = dp[i-1][0]
        
for j in range(b):
    if A[0] == B[j]:
        dp[0][j] = A[0]
    else:
        dp[0][j] = dp[0][j-1]

for i in range(1,a):
    for j in range(1,b):
        if len(dp[i][j-1]) >= len(dp[i-1][j]):
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j]
        if A[i] == B[j] and len(dp[i-1][j-1]) >= len(dp[i][j]):
            dp[i][j] = dp[i-1][j-1] + A[i]
            
ans = dp[-1][-1]
print(len(ans))
if len(ans):
    print(ans)
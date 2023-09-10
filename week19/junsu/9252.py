import sys

a = '0' + sys.stdin.readline().rstrip()
b = '0' + sys.stdin.readline().rstrip()
la = len(a)
lb = len(b)

dp = [['' for _ in range(lb)] for _ in range(la)]

for i in range(1,la):
    for j in range(1,lb):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + a[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

ans = dp[-1][-1]
if len(ans):
    print(len(ans),ans,sep='\n')
else:
    print(len(ans))

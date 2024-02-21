# 최장 공통 부분 수열 문제 : 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
import sys
input = sys.stdin.readline
column = list(map(str, input().rstrip()))
row = list(map(str, input().rstrip()))
column.insert(0, 0)
row.insert(0, 0)
column_num = len(column)
row_num = len(row)
# print(column_num)
# print(row_num)
dp = [[0] * (column_num) for _ in range(row_num)]
for i in range(1, row_num):
  # dp[i] = dp[i-1]
  for j in range(1, column_num):
    if row[i] == column[j]:
      dp[i][j] = dp[i-1][j-1] + 1
      # dp[i-1][j+1] = dp[i][j]
    # elif i == 1 and row[i] != column[j]:
    #   dp[i][j] = dp[i][j-1]
    else:
      if dp[i][j-1] > dp[i-1][j]:
        dp[i][j] = dp[i][j-1]
      else: dp[i][j] = dp[i-1][j]
print(dp[-1][-1])

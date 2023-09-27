# n*m * m*k =  n*m*k (곱셈연산의수)
# 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

# 행렬 n개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램!!
# 입력으로 주어진 행렬의 순서 바꾸면 안 된다.
# 5*3 * 3*2 = 5*3*2 (30)
# 5*2 * 2*6 = 5*2*6 (60)

# 3*2 * 2*6 = 3*2*6 (36)
# 5*3 * 3*6 = 5*3*6 (90)

# n = int(input())
# for _ in range(n):
#   a, b

N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]

dp = [[float('inf')] * N for _ in range(N)]
for i in range(N):
  dp[i][i] = 0

for k in range(1, N):
  for i in range(N - k):
    for j in range(i, i + k):
      s, m, e = i, j, i+k
      dp[s][e] = min(dp[s][e], dp[s][m] + dp[m + 1][e] + matrix[s][0] * matrix[m][1] * matrix[e][1])
print(dp[0][N-1])
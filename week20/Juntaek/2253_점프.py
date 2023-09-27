# 이동은 앞으로만 돌 번호 증가하는 순서대로
# 처음에는 한 칸만 점프
# 점프는 x-1, x, x+1 칸 점프가능
# 올라갈 수 없는 돌들도 중간에 존재
# 위 조건 만족하면서 1~N번 돌까지 점프를 할 때, 최소의 점프 횟수를 구하는 프로그램 작성!
# 2 (0, 1, 2)
# 4 (1, 2, 3)
# 7 (2, 3, 4)
# 10 (2, 3, 4)
# 14 (3, 4, 5)
# 19
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [[float('inf')] * (int((2 * N) ** 0.5) +2) for _ in range(N + 1)]
dp[1][0] = 0
stone_set = set()
for _ in range(M):
  stone_set.add(int(input()))
for i in range(2, N + 1):
  if i in stone_set:
    continue
  for j in range(1, int((2 * i) ** 0.5) +1):
    dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1] + 1)

if min(dp[N]) == float('inf'):
  print(-1)
else:
  print(min(dp[N]))


# 수열 a가 주어질거야. 거기서 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성!
n = int(input())
a = list(map(int, input().split()))

# 배열에서 첫번째부터 하나씩 뒤에랑 비교해서 1번째가 0번째보다 크다? 그럼 1번째로 업데이트 시켜준 후 cnt += 1 그 다음 2번째애랑 1번째애 비교해서 더 크다? 그럼 업데이트 작으면 업데이트 노노
# 이중 for문을 써서 해야함
answer = []
# for i in range(1, n):
#   if ret < a[i]:
#     ret = a[i]
#     cnt += 1

for i in range(n-1):
  ret = a[i]
  cnt = 1
  for j in range(i+1, n):
    if ret < a[j]:
      ret = a[j]
      # print(ret, end="")
      cnt += 1
  answer.append(cnt)
  # print(answer)
print(max(answer))

# 풀이 코드
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
  for j in range(i):
    if a[i] > a[j]:
      dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
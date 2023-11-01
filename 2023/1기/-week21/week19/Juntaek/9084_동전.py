# 1, 5, 10, 50, 100, 500
# ex) 30 : 1 * 30개, 10 * 2 + 5 * 2
# 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.
# n가지 동전으로 금액 m을 만드는 모든 방법의 수를 하나씩 출력!


# 풀이 코드 (https://d-cron.tistory.com/23)
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  coins = list(map(int, input().split()))
  # print(coins)
  coins.insert(0,0)
  # print(coins)
  M = int(input())

  dp = [[0] * (M+1) for _ in range(N+1)]
  for i in range(N+1):
    dp[i][0] = 1

  for i in range(1, N+1):
    for j in range(1, M+1):
      dp[i][j] = dp[i-1][j]
      if j - coins[i] >= 0:
        dp[i][j] += dp[i][j-coins[i]]
  print(dp[N][M])

  # 풀이 코드2 (https://velog.io/@whddn0221/%EB%B0%B1%EC%A4%80-9084-%EB%8F%99%EC%A0%84-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
  import sys
  input = sys.stdin.readline

  t = int(input())
  for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    d = [0] * (m+1)
    d[0] = 1

    for coin in coins:
      for i in range(m+1):
        if i >= coin:
          d[i] += d[i-coin]

    print(d[m])
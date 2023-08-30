# n가지 종류의 동전 존재
# n가지 종류의 동전 사용해서 합이 k원이 되도록! but 동전 개수는 최소로
# 각 동전은 몇개라도 사용가능
# 요구사항을 데이터로 바라보기
# 5를 3번 곱해서 15를 만드는게 동전이 가장 적게듬.
# 주어진 입풋을 어떻게 활용할 것인가

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
check = [0 for _ in range(k+1)]
que = deque()
for coin in coins:
  if coin > k:
    continue
  que.append([coin, 1])
  check[coin] = 1

flag = True
while que:
  val, cnt = que.popleft()
  if val == k:
    print(cnt)
    flag = False
    break

  for coin in coins:
    if val + coin > k:
      continue
    if check[val+coin] == 0:
      check[val+coin] = 1
      que.append([val+coin, cnt+1])

if flag:
  print(-1)

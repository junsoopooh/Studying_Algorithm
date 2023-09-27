# N가지 동전을 적절히 사용해서 그 가치의 합을 K로 만들어야 함
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램!
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]
# # print(coins)
# coins.sort(reverse=True)
# cnt = 0
# for coin in coins:
#   while coin <= k:
#     k -= coin
#     cnt += 1

# print(cnt)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
min_coin_num = 0
coins.sort(reverse=True)
for i in range(len(coins)):
  if coins[i] <= k:
    num = k // coins[i]
    k -= coins[i] * num
    min_coin_num += num
print(min_coin_num)
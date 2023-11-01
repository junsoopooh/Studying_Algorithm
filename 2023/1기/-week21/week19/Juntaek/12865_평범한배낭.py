# 배낭을 가치있게 싸보자!
# n: 물건개수
# w: 무게, v: 가치
# 최대 k만큼의 무게만을 넣을 수 있는 배낭 들고가기.
# 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
# 가치순으로 먼저 정렬 후 무게순으로 다시 한번 정렬

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [[0] * (k+1) for _ in range(k+1)]

things = []
for _ in range(n):
  things.append(list(map(int, input().split())))
things.sort()
# print(arr)
# print(things)
for i in things:
  w, v = i[0], i[1]
  arr[w][w] = v
# print(arr)
answer = things[0][1]
for i in range(1, n):
  w, v = things[i][0], things[i][1]
  if k - w >= 0:
    arr[w][w] = arr[k-w][k-w] + v
    answer = max(answer, arr[w][w])
    # print(arr[w][w])
    # print(answer)
print(answer)
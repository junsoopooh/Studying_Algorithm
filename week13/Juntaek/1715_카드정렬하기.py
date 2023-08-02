# 최소 묶음 순으로 비교하는게 최소 숫자가 나오지 않을까?
import sys
input = sys.stdin.readline
n = int(input())
list = []
for _ in range(n):
  list.append(int(input()))
list.sort()
if len(list) == 1:
  print(0)
else:
  answer = 0
  while len(list) > 1:
    temp1 = list.pop(0)
    temp2 = list.pop(0)
    answer += temp1 + temp2
    list.append(answer)
    list.sort()
print(answer)

### heapq 사용 ###
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
card_deck = []
for _ in range(n):
  hq.heappush(card_deck, int(input()))

if len(card_deck) == 1:
  print(0)
else:
  answer = 0
  while len(card_deck) > 1:
    temp1 = hq.heappop(card_deck)
    temp2 = hq.heappop(card_deck)
    answer += temp1 + temp2
    hq.heappush(card_deck, temp1+temp2)

  print(answer)

  # 아래 코드로 백준 채점 시 런타임 에러 발생..
  while card_deck:
    temp1 = hq.heappop(card_deck)
    temp2 = hq.heappop(card_deck)
    answer += temp1 + temp2
    if len(card_deck) == 0:
      print(answer)
      break
    hq.heappush(card_deck, temp1 + temp2)
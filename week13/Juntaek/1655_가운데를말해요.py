# 정수를 외치면 말한 수 중에서 중간값 외치기
# 외친 수의 개수가 짝수개면 두 수 중 작은 수 말하기

import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
leftHeap = []
rightHeap = []
for i in range(n):
  num = int(input())

  if len(leftHeap) == len(rightHeap):
    hq.heappush(leftHeap, -num)
  else:
    hq.heappush(rightHeap, num)

  if rightHeap and rightHeap[0] < -leftHeap[0]:
    leftValue = hq.heappop(leftHeap)
    rightValue = hq.heappop(rightHeap)

    hq.heappush(leftHeap, -rightValue)
    hq.heappush(rightHeap, -leftValue)

  print(-leftHeap[0])
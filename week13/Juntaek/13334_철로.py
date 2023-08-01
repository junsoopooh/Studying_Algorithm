# 집과 사무실사이의 거리가 철로의 위치 보다 작아야 함.
# start + d 사이에 집과 사무실의 좌표가 들어와야 함.

# 입력값의 첫번째 인덱스가 더 작은 값이 들어오도록 하고 싶어
# 집과 사무실 사이의 거리를 계산해서 d보다 작은 놈들만 추리기?
# 리스트에 입력값을 쫙 받고 두 숫자 중 더 작은 숫자랑 거리를 튜플로 저장?

import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
roads, data = [], []

for _ in range(n):
  data.append(sorted(list(map(int, input().split()))))
d = int(input())

for road in data:
  s, e = road
  if (e - s) <= d:
    roads.append(road)

roads.sort(key=lambda x: x[1])

answer = 0
heap = []

for road in roads:
  if not heap:
    hq.heappush(heap, road)
  else:
    while heap[0][0] < road[1] - d:
      hq.heappop(heap)
      if not heap:
        break
    hq.heappush(heap, road)
  answer = max(answer, len(heap))

print(answer)
# 전 지점의 오른쪽 x좌료를 스택에 넣고 기억해야 하나? 우선순위 큐를 어떻게 활용할까?

import sys
import heapq as hq
input = sys.stdin.readline

events = []
for i in range(n):
  L, H, R = map(int, input().split())
  events.append([L, -H, R])
  events.append([R, 0, 0])

events.sort()
print(events)

res = [[0, 0]]
live = [(0, float('inf'))]

for pos, negH, R in events:
  print("현재 iive: ", live)
  while live[0][1] <= pos:
    hq.heappop(live)
  if negH:
    hq.heappush(live, (negH, R))

  if res[-1][1] != -live[0][0]:
    res.append(f'{pos} {-live[0][0]} ')
print("".join(res[1:]))
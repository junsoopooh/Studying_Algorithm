# 최대 힙 사용
# 자연수 x가 주어지면 배열에 넣는 연산
# 0가 입력으로 들어오면 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거하는 연산
n = int(input())
list = []
for _ in range(n):
  data = int(input())
  if data != 0:
    list.append(data)
  else:
    if len(list) == 0:
      print(0)
    else:
      list.sort()
      print(list.pop())


# heapq 활용 #
import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
  x = int(input())
  if x:
    hq.heappush(heap, (-x, x))
  else:
    if len(heap) == 0:
      print(0)
    else:
      print(hq.heappop(heap)[1])
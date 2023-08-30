import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = []
room = []
for _ in range(n):
  start, end = map(int, input().split())
  arr.append([start, end])

# 일단 시작시간 기준으로 수업들을 정렬
arr.sort()
# print(arr)

# 다음 강의의 시작시간이 이전 강의의 종료시간보다 이르면 새로운 강의실 추가로 개설
# 만약 다음강의 시작시간이 이전강의 종료시간보다 느리면 강의실 개설할 필요 없음
for i in range(len(arr)):
  if room:
    if room[0] <= arr[i][0]:
      heapq.heappop(room)
      heapq.heappush(room, arr[i][1])
      # print(room)
    else:
      heapq.heappush(room, arr[i][1])
      # print(room)
  else:
    heapq.heappush(room, arr[i][1])
    # print(room)
print(len(room))
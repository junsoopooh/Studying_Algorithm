# n이 주어지면 1부터 n까지 for문을 돌려
# 만약 i가 홀수면 popleft
# 만약 i가 짝수면 popleft해서 queue에 append
# 만약에 queue의 길이가 1이면 break하고 마지막에 남은 수 출력
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque([i for i in range(1, n+1)])
print(queue)
# for i in range(1, n+1):
#     if (i%2 == 1):
#       queue.popleft()
#     else:
#       data = queue.popleft()
#       queue.append(data)
    # if len(queue) == 1:
    #    print(queue[-1])
while len(queue) != 1:
  queue.popleft()
  data = queue.popleft()
  queue.append(data)
print(queue[0])
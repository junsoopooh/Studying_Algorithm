# 큐2
import sys
input = sys.stdin.readline
n = int(input())
queue = []
for _ in range(n):
  data = input().split()
  # print(data)
  if data[0] == 'push':
    queue.append(data[1])
  elif data[0] == 'pop':
    if queue:
      queue.pop(0)
    else:
      print(-1)
  elif data[0] == 'size':
    print(len(queue))
  elif data[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif data[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif data[0] == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)
      
# deque 사용
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])
for i in range(n):
  data = input().split()
  if data[0] == 'push':
    queue.append(data[1])
  elif data[0] == 'pop':
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif data[0] == 'size':
    print(len(queue))
  elif data[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif data[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif data[0] == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)
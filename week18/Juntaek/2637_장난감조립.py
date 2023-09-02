# 중간 부품 : 기본 부품을 이용하여 만들어진다.
# 장난감 완제품을 조립하기 위해 필요한 기본 부품의 종류별 개수를 계산하는 프로그램 작성!
# N : 완제품의 번호
# 하나의 완제품을 조립하기 위해 필요한 기본 부품의 수를 한 줄에 하나씩 출력(중간 부품 출력x) 반드시 부품의 번호가 작은 것부터 큰 순서로.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
connect = [[] for _ in range(n + 1)]
needs = [[0] * (n+1) for _ in range(n+1)]
q = deque()
degree = [0] * (n+1)
for _ in range(int(input())):
  a, b, c = map(int, input().split())
  connect[b].append((a, c))
  degree[a] += 1

for i in range(1, n+1):
  if degree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  for next, next_need in connect[now]:
    if needs[now].count(0) == n + 1:
      needs[next][now] += next_need
    else:
      for i in range(1, n+1):
        needs[next][i] += needs[now][i] * next_need

    degree[next] -= 1
    if degree[next] == 0:
      q.append(next)

for x in enumerate(needs[n]):
  if x[1] > 0:
    print(*x)
print(needs)
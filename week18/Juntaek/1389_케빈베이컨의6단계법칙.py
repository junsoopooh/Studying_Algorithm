# 6단계 이내에서 모든 사람들은 서로 아는 사람으로 연결
# 임의의 두 사람이 최소 몇 단계에 이어질 수 있는가?
# 천민호, 이강호
# 천민호, 최백준
# 최백준, 김선영
# 김선영, 김도현
# 김도현, 민세회
# 케빈 베이커의 수가 가장 적은 사람 찾기!
# N: 유저의 수
# M: 친구 관계의 수
# dfs로 찾을 건데 1~N까지 탐색을 할거야
# 1이 들어오면 1 이외에 값들을 목표값으로 두고 탐색
# i가 2인데 그래프상에서 1과 연결된 2가 나오면 거기서 cnt를 계산함과 동시에 break을 때린다?
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#   a, b = map(int, input().split())
#   graph[a].append(b)
#   graph[b].append(a)

# answer = []

# def dfs(start):
#   visited[start] = True
#   cnt = 1
#   for num in range(1, N+1):
#     if not visited[num]:
#       for i in graph[i]:
#         if not visited[i]:
#           if num == i:
#             answer.append(cnt)
#             break
#           else:
#             dfs(i)

# for i in range(1, N+1):
#   visited = [False * (N+1)]
#   if not visited[i]:
#     for num in range(N+1):
#   if not visited[i]:

#     dfs(i)

# bfs 풀이코드
import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(graph, start):
  num = [0] * (n+1)
  visited = [start]
  queue = deque([start])

  while queue:
    a.queue.popleft()
    for i in graph[a]:
      if i not in visited:
        num[i] = num[a] + 1
        visited.append(i)
        queue.append(i)
    return sum(num)

result = []
for i in range(1, n+1):
  result.append(bfs(graph, i))

print(result.index(min(result))+1)

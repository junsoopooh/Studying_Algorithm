# N개의 섬으로 이루어진 나라
# 몇개의 섬 사이에는 다리가 설치
# 공장에서 다른 공장으로 물품 수송 필요성
# 그런데 각각의 다리마다 중량제한이 존재
# 중량제한을 초과하는 양의 물품이 다리 건너면 다리 무너진다.
# 서로 같은 두 섬 사이에 여러 개 다리 존재 가능
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램!
# 모든 다리는 양방향
# 마지막은 공장이 위치해 있는 섬의 번호
# 그럼 1에서 3으로 옮겨야 한다는 거지?
# 1-2-3, 1-3
# 1에서 3으로 한번에 3만큼 옮길 수 있어서 답이 3출력

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] * (n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

# 그럼 start에서 end까지 한번에 갈 수 있는 경로만 탐색해서 찾아내고
# 만약에 한번에 가는 경로가 2개 이상이다? 그럼 중량제한이 최대인 경로를 뽑아내면 되는거 아니야?

# def dfs(start):
#   visited[start] = True
#   for i in graph[start]:
#     if not visited[i]:
#       visited[i] = True
#       dfs(i)
# # bfs를 써야할까? start랑 연결된 애들이 쫙 있을텐데 그 중에서 한번에 end로 가는 경로를 찾는거야.
# def bfs(start):
#   q = deque([start])
#   while q:
#     now = popleft()
#     for i in graph[now]:
#       if not visited[i] and i == end:
#         answer.append()
#         visited[now] = True
#         q.append()


# union-find 풀이 코드 (https://hbj0209.tistory.com/132)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []

def find(c):
  if par[c] == c:
    return c
  else:
    par[c] = find(par[c])
  return par[c]

def union(a, b):
  a, b = find(a), find(b)
  par[max(a, b)] = min(a, b)

def check(a, b):
  return find(a) == find(b)

par = [i for i in range(N+1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  graph.append([-c, a, b])
ts, te = map(int, input().split())

graph.sort()
for i in graph:
  c, a, b = i[0], i[1], i[2]
  c = abs(c)
  union(a, b)
  if check(ts, te):
    print(c)
    break
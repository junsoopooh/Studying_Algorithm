# 풀이 코드 (https://velog.io/@whddn0221/%EB%B0%B1%EC%A4%80-1432-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%88%98%EC%A0%95-%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-mrltwcp5)
import heapq

n = int(input())
graph = [[] for _ in range(n + 1)]
outdegree = [0] * (n+1)
result = [0] * (n+1)

for i in range(1, n+1):
  connection = list(map(int, input()))
  for idx, val in enumerate(connection):
    if val == 1:
      graph[idx + 1].append(i)
      outdegree[i] += 1

def topology_sort(n):
  heap = []
  for i in range(1, n+1):
    if outdegree[i] == 0:
      heapq.heappush(heap, -i)

  while heap:
    now = -heapq.heappop(heap)
    result[now] = n

    for connected_node in graph[now]:
      outdegree[connected_node] -= 1
      if outdegree[connected_node] == 0:
        heapq.heappush(heap, -connected_node)
    n -= 1

topology_sort(n)

if result.count(0) > 2:
  print(-1)
else:
  print(' '.join(map(str, result[1:])))
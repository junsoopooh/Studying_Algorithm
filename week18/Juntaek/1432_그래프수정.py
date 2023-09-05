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
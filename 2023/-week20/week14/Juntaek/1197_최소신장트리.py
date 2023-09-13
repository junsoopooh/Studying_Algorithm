import sys

def find(a):
  if a == parent[a]:
    return a

  parent[a] = find(parent[a])
  return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)

  if b < a:
    parent[a] = b
  else:
    parent[b] = a

v, e = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]
graph.sort(key=lambda x: x[2])
parent = [i for i in range(v+1)]
answer = 0

for s, e, w in graph:
  if find(s) != find(e):
    union(s, e)
    answer += w
print(answer)
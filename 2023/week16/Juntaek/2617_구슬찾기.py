import sys
input = sys.stdin.readline

# 중간에 구슬이 절대로 올 수 없는 경우는 자신보다 더 무거운 구슬이 n//2개 있는 경우
# 혹은 더 가벼운 구슬이 n//2개 있는 경우
# 이때 자신보다 더 무거운 리스트 더 가벼운 리스트 나눠서 입력을 받은 후
# dfs 돌려서 자신보다 무겁거나, 가벼운 구슬이 몇개인지 카운트하면됨
# 카운트했는데 만약 n//2보다 많다? 그럼 그때가 중간이 될 수 없는 구슬임
n, m = map(int, input().split())
graph_h = [[] for _ in range(n+1)]
graph_l = [[] for _ in range(n+1)]
for _ in range(m):
  heavy, light = map(int, input().split())
  graph_h[light].append(heavy)
  graph_l[heavy].append(light)
# print(graph_h)
# print(graph_l)
mid = (n+1)/2
ret = 0
def dfs_h(start):
  global cnt
  # visited[start] = True
  for i in graph_h[start]:
    if not visited[i]:
      # print(visited)
      visited[i] = True
      cnt +=1
      dfs_h(i)

def dfs_l(start):
  global cnt2
  # visited[start] = True
  for i in graph_l[start]:
    if not visited[i]:
      # print(visited)
      visited[i] = True
      cnt2 += 1
      dfs_l(i)

# visited = [False for _ in range(n+1)]
for i in range(1, n+1):
  visited = [False for _ in range(n+1)]
  if not visited[i]:
    cnt = 0
    cnt2 = 0
    dfs_h(i)
    dfs_l(i)
    if cnt >= mid:
      ret += 1
    if cnt2 >= mid:
      ret += 1
print(ret)

# 다른 풀이
# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())

# bigger_lst = [[] for _ in range(N+1)]
# smaller_lst = [[] for _ in range(N+1)]
# mid = (N+1)/2

# for i in range(M):
#   a, b = map(int, input().split())
#   bigger_lst[b].append(a)
#   smaller_lst[a].append(b)

# def dfs(arr, n):
#   global cnt
#   for i in arr[n]:
#     if not visited[i]:
#       visited[i] = True
#       cnt += 1
#       dfs(arr, i)

# answer = 0
# for i in range(1, N+1):
#   visited = [False] * (N+1)
#   cnt = 0
#   dfs(bigger_lst, i)
#   if cnt >= mid:
#     answer += 1
#   cnt = 0
#   dfs(smaller_lst, i)
#   if cnt >= mid:
#     answer += 1
# print(answer)
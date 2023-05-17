import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
visited = [False]*n
cnt = 0

def pick(x, tmp):
    global cnt
    if x == 0:
        if tmp == s:
            cnt += 1
            return
        else:
            return
    
    for i in range(n):
        if not visited[i]:
            tmp += nums[i]
            visited[i] = True
            pick(x-1, tmp+nums[i])

for i in range(n):
    visited = [False]*n
    pick(i, 0)
print(cnt)

# def dfs(tmp):
#     global cnt
#     if tmp == s:
#         cnt += 1
#         return

#     for i in range(n):
#         if not visited[i]:
#             tmp += nums[i]
#             visited[i] = True
#             dfs(tmp)
#             visited[i] = False
#             tmp -= nums[i]

# dfs(0)
# print(cnt)

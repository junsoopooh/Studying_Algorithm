import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
ans = []
cnt = 0
visited = [False]*n

# 정답 코드
# def solve(start):

#     global cnt
#     if sum(ans) == s and len(ans) > 0:
#         cnt += 1
    
#     for i in range(start,n):
#         ans.append(nums[i])
#         solve(i+1)
#         ans.pop()
        
# solve(0)
# print(cnt)

# 배준수 오답 코드
# def pick(x, tmp):
#     global cnt
#     if x == 0:
#         if tmp == s:
#             cnt += 1
#             return
#         else:
#             return
    
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             tmp += nums[i]
#             x -= 1
#             pick(x,tmp)
#             x += 1
#             tmp -= nums[i]

# for i in range(1,n+1):
#     visited = [False]*n
#     pick(i, 0)
# print(cnt)

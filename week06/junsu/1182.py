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

# 내 코드는 dfs 깊이를 직접설정해줬음. 즉 n번해야함. dfs자체도 n에 관한 loop인데 n^2이 되버림.
# 또 백트래킹에서 false처리를 하면안됌.
# 지하 1층 가서 없으면 2층을 가봐야하는데 일단 복귀함.
# A동 1층,B,C,D,E 확인하고 그다음 A동1,2층, B,C, .. 반복
# 개쓸데없이 dfs의 장점을 잃었다.

# 오히려 0부터 시작해서 더해도 된다!

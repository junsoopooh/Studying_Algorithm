# n장 중에서 k장을 선택해서 숫자 조합을 만든다.
# 21이랑 12는 다름.. 중복허용 안함.
import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
nums = []
for _ in range(n):
    nums.append(int(input().rstrip()))

# n = 6
# k = 3
# nums = [72, 2, 12, 7, 2, 1]

visited = [False] * n
perm = []

result = []
def dfs(N):
    if N == 0:
        re = ""
        for e in perm:
            re += str(e)
        result.append(re)
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            perm.append(nums[i])
            dfs(N-1)
            visited[i] = False
            perm.pop()

dfs(k)
print(len(set(result)))
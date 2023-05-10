# 3개의 카드 조합의 합이 목표 합에 가장 가까운(min_diff) 조합의 합 출력
import sys
input = sys.stdin.readline

N, target = map(int, input().split())
nums = list(map(int, input().split()))

# N = 5
# target = 21
# nums = [5, 6, 7, 8, 9]

visited = [False]*N

comb = []
# result = []
min_diff = float("inf")
answer = 0
def dfs(n, start):
    global answer, min_diff # 비효율적 개선 필요!
    if n == 0:
        if sum(comb) <= target:
            if min_diff > target - sum(comb):
                min_diff = target - sum(comb)
                answer = sum(comb)
            # result.append(sum(comb))
        return
    for i in range(start, N):
        if visited[i] == False:
            visited[i] = True
            comb.append(nums[i])
            dfs(n-1, i+1)
            visited[i] = False
            comb.pop()

dfs(3, 0)
print(answer)

# 생각해보면 값을 다 넣어주고 그 값중에 max값을 출력해주면 목표합에 가장 가까운 값이 되는 것 같기도...?
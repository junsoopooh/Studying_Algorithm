# 9명 중에 7명 조합 중 그 숫자의 합이 100인 경우 오름차순 출력

# 반례
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 94
# 95

import sys
input = sys.stdin.readline

height = []
for _ in range(9):
    height.append(int(input()))
# height.sort()
# height = [20, 7, 23, 19, 10, 15, 25, 8, 13]

visited = [False] * len(height)

comb = []
# result = []
def dfs(n, start):
    if n == 0:
        if sum(comb) == 100:
            comb.sort()
            print(*comb, sep='\n')
            exit() # 이거 절대 쓰면 안됨.... 개선 필요!!!!
            # result.append(comb[:])
        return
    for i in range(start, len(height)):
        if visited[i] == False:
            visited[i] = True
            comb.append(height[i])
            dfs(n-1, i+1)
            visited[i] = False
            comb.pop()

dfs(7, 0)
# print(result)
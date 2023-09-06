import sys
from heapq import heappop, heappush
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def cal():
    max_val = 0
    for i in range(m):
        for j in range(m):
            if j == i:
                continue
            for k in range(m):
                ans = 0
                if k == i or k == j:
                    continue
                for person in range(n):
                    arr = []
                    heappush(arr, -1*graph[person][i])
                    heappush(arr, -1*graph[person][j])
                    heappush(arr, -1*graph[person][k])
                    tmp = heappop(arr)
                    tmp *= -1
                    ans += tmp
                max_val = max(max_val, ans)
    return max_val


answer = cal()
print(cal())

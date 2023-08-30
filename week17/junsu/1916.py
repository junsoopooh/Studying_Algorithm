import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, a, c = map(int, sys.stdin.readline().split())
    graph[s].append([c, a])
start, arrive = map(int, sys.stdin.readline().split())


def search(x):
    cost = [10**9 for _ in range(n+1)]
    cost[x] = 0
    arr = []
    heappush(arr, [0, x])
    while arr:
        price, now = heappop(arr)
        if price > cost[now]:
            continue
        for money, next in graph[now]:
            new_money = price + money
            if new_money < cost[next]:
                cost[next] = new_money
                heappush(arr, [new_money, next])
    return cost


ans = search(start)
print(ans[arrive])

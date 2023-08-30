import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
coin = set()
for _ in range(n):
    tmp = int(sys.stdin.readline())
    coin.add(tmp)
coin = list(coin)
visited = [0 for _ in range(k+1)]


def bfs():
    arr = deque()
    for i in coin:
        if i == k:
            return 1
        if i < k:
            visited[i] = 1
            arr.append(i)
    while arr:
        money = arr.popleft()
        for i in coin:
            if money+i > k:
                continue
            elif money+i == k:
                return visited[money]+1
            elif money+i <= k and not visited[money+i]:
                arr.append(money+i)
                visited[money+i] = visited[money]+1
    return -1


ans = bfs()
print(ans)

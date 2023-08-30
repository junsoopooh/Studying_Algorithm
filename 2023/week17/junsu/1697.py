import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
sys.setrecursionlimit = 10**6

dp = [0 for _ in range(10**6)]
queue = deque()
queue.append([n, 0])

while True:
    x, t = queue.popleft()
    if x == k:
        print(t)
        break
    if 2*x < 10**6 and not dp[2*x]:
        dp[2*x] = t+1
        queue.append([2*x, t+1])

    if x+1 < 10**6 and not dp[x+1]:
        dp[x+1] = t+1
        queue.append([x+1, t+1])

    if x-1 >= 0 and x-1 < 10**6 and not dp[x-1]:
        dp[x-1] = t+1
        queue.append([x-1, t+1])

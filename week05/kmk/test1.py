"""
소수 경로
문제: https://www.acmicpc.net/problem/1963
"""
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

# 에라토스테네스의 체
limit = 10000

nums = [1] * limit

for i in range(2, int(limit**0.5)+1):
    if nums[i]:
        for j in range(i*i, limit, i):
            nums[j] = 0

prime = [i for i in range(1000, limit) if nums[i]]

# 한 자리수만 다른지 체크하는 메소드
def check(x, y):
    x, y = str(x), str(y)
    c = 0
    for i in range(4):
        if x[i] != y[i]:
            c += 1
    return c == 1

def bfs(x, y):
    q = deque()
    q.append([x, 0])
    visited = [0] * limit
    visited[x] = 1

    while q:
        cur, cnt = q.popleft()
        if cur == y:
            return cnt
        for p in prime:
            if not visited[p] and check(cur, p):
                visited[p] = 1
                q.append([p, cnt + 1])
    return -1

for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print(0)
        continue

    res = bfs(a, b)
    print(res if res != -1 else -1)
import sys
input = sys.stdin.readline
from collections import deque

# N명이 게임을 할 때, K번째로 수건을 받는 사람은?
n, k = map(int, input().split())

if k == 1:
    print(1)
else:
    values = deque([i+1 for i in range(n)])

    # 리턴 변수
    result = values[0]

    for _ in range(k-1):
        values.popleft()
        values.rotate(-1)

        result = values[0]

    print(result)
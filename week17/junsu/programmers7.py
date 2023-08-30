# 전력망을 둘로 나누기
from collections import deque


def solution(n, wires):
    answer = n
    d = len(wires)
    for i in range(d):
        arr = deque()
        arr.append(0)
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        visited[0] = True
        for j in range(d):
            if j == i:
                continue
            else:
                a, b = wires[j]
                graph[a-1].append(b-1)
                graph[b-1].append(a-1)
        while arr:
            now = arr.popleft()
            for x in graph[now]:
                if not visited[x]:
                    visited[x] = True
                    arr.append(x)
        cnt = visited.count(True)
        cnt = abs(n-2*cnt)
        answer = min(answer, cnt)
    return answer

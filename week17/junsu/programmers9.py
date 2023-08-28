# 합승 택시 요금
# 1차 시도 85/100
from heapq import heappop, heappush
from collections import deque


def solution(n, s, a, b, fares):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for way in fares:
        c, d, f = way
        graph[c][d] = f
        graph[d][c] = f

    def search(start, end):
        if start == end:
            return 0
        visited = [0 for _ in range(n+1)]
        arr = deque()
        arr.append(start)
        while arr:
            now = arr.popleft()
            for next in range(1, n+1):
                if next == now:
                    continue
                if graph[now][next]:
                    if not visited[next] or visited[next] > visited[now] + graph[now][next]:
                        visited[next] = visited[now] + graph[now][next]
                        arr.append(next)
                    else:
                        continue
        if visited[end]:
            return visited[end]
        else:
            False

    answer = search(s, a)+search(s, b)
    for i in range(1, n+1):
        if s == i or not search(s, i):
            continue
        tmp = search(s, i) + search(i, a) + search(i, b)
        answer = min(tmp, answer)
    return answer


# 2차시도 100/100


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    answer = 1e9
    for way in fares:
        c, d, f = way
        graph[c].append([d, f])
        graph[d].append([c, f])

    def search(start, end):
        visited = [1e9 for _ in range(n+1)]
        arr = []
        heappush(arr, [0, start])
        visited[start] = 0
        while arr:
            cnt, now = heappop(arr)
            if visited[now] < cnt:
                continue

            for x in graph[now]:
                tmp_now, tmp_cnt = x[0], x[1]
                tmp_cnt += cnt
                if tmp_cnt < visited[x[0]]:
                    visited[tmp_now] = tmp_cnt
                    heappush(arr, [tmp_cnt, tmp_now])
        return visited[end]

    for i in range(1, n+1):
        answer = min(answer, search(s, i)+search(i, a)+search(i, b))
    return answer

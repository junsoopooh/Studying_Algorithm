# 디스크 컨트롤러
from heapq import heappop, heappush


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    waiting = []
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heappush(waiting, [j[1], j[0]])
        if waiting:
            working = heappop(waiting)
            start = now
            now += working[0]
            answer += (now-working[1])
            i += 1
        else:
            now += 1
    answer //= len(jobs)
    return answer

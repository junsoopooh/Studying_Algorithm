# [덧칠하기](https://school.programmers.co.kr/learn/courses/30/lessons/161989)

from heapq import heappop, heappush

def solution(n, m, section):
    answer = 0
    arr = []
    for x in section:
        heappush(arr,x)
    idx = heappop(arr)
    end = idx + m -1
    cnt = 1
    while arr:
        if arr[0] <= end:
            heappop(arr)
            continue
        else:
            idx = heappop(arr)
            end = idx + m -1
            cnt += 1
    return cnt
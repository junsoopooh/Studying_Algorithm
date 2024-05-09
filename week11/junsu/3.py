# [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)

from heapq import heappush, heappop

def solution(scoville, K):
    arr = []
    answer = 0
    for x in scoville:
        heappush(arr,x)
    while arr[0] < K and len(arr) >=2:
        tmp1 = heappop(arr)
        tmp2 = heappop(arr)
        new_value = tmp1 + 2*tmp2
        heappush(arr,new_value)
        answer += 1
    if len(arr) == 1 and arr[0] < K:
        return -1
    return answer
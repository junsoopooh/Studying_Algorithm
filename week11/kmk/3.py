"""
더 맵게
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        min_value = min(a, b)
        max_value = max(a, b)
        heapq.heappush(scoville, min_value + max_value * 2)
        answer += 1

    return answer if scoville[0] >= K else -1

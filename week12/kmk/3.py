"""
H-Index
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""
"""
어차피 최대 인용횟수는 주어진 배열의 최대값이므로 0~최대값까지 for문 돌면서 이분탐색으로 해결
"""

from bisect import bisect_left

def solution(c):
    ans = 0

    c.sort()

    for i in range(c[-1] + 1):
        idx = bisect_left(c, i)
        if len(c[:idx]) < i <= len(c[idx:]):
            ans = max(ans, i)

    return ans
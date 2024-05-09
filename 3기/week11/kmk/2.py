"""
소수 만들기
문제: https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""

from itertools import combinations

def solution(nums):
    ans = 0
    n = sum(nums)

    prime = [1] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i + i, n + 1, i):
                prime[j] = 0

    for e in combinations(nums, 3):
        if prime[sum(e)]:
            ans += 1
    return ans
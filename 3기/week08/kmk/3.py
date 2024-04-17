"""
의상
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""

from collections import Counter


def solution(clothes):
    dic = Counter([j for i, j in clothes])

    ans = 1

    for k in dic.values():
        ans *= (k + 1)

    return ans - 1
"""
실패율
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42889
"""

from collections import Counter

def solution(N, stages):
    n = len(stages)
    ls = sorted([i, j] for i, j in Counter(stages).items() if i <= N)

    for i in range(len(ls)):
        tmp = ls[i][1]
        ls[i][1] /= n
        n -= tmp

    ls.sort(key=lambda x: (-x[1], x[0]))

    ls = [i for i, j in ls]

    return ls + [i for i in range(1, N + 1) if i not in ls]
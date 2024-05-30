"""
후보키
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42890
"""

from itertools import combinations
from collections import Counter


def solution(relation):
    # 속성 개수
    n = len(relation[0])

    # 전체 튜플 수
    m = len(relation)

    # 유일성 체크 함수
    def check_unique(attribute):
        tuples = []
        for column in relation:
            tuples.append(tuple([column[i] for i in attribute]))

        if len(set(tuples)) == m:
            return True

        return False

    # 유일성 만족
    unique = []

    # 속성 조합 1개 ~ n개
    for i in range(1, n + 1):
        for attribute in combinations([a for a in range(n)], i):
            if check_unique(attribute):
                unique.append(attribute)

    res = [0] * len(unique)

    # 최소성 확인
    for i in range(len(unique)):
        for j in range(len(unique)):
            if res[i] or res[j]:
                continue
            if i != j:
                a, b = Counter(unique[i]), Counter(unique[j])
                c = a + b
                if len(c) == len(b):
                    res[j] = 1

    return len(unique) - sum(res)

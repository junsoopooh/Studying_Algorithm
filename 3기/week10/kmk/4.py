"""
메뉴 리뉴얼
문제: https://school.programmers.co.kr/learn/courses/30/lessons/72411
"""

"""
1. 딕셔너리에 각 코스의 개수에 따라 모든 조합 저장
2. answer 리스트에 각 코스의 개수에 따라 최대 주문된 갯수 저장 예시를보면 [4, 3, 2] 저장
3. 마지막으로 딕셔너리에서 문자열 코스 길이하고 비교해서 걸러내면 된다.
"""

from collections import Counter
from itertools import combinations


def solution(orders, course):
    s = Counter()

    answer = []

    for num in course:
        for o in orders:
            if len(o) < num:
                continue

            for elem in list(combinations(o, num)):
                s["".join(sorted(elem))] += 1
        cnt = 0
        for i, j in s.items():
            if len(i) == num:
                cnt = max(cnt, j)
        answer.append(cnt)

    f = []

    for i in range(len(answer)):
        if answer[i] == 0:
            continue
        for a, b in s.items():
            if len(a) == course[i]:
                if b == answer[i] and b >= 2:
                    f.append(a)

    return sorted(f)
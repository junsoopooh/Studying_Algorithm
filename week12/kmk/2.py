"""
덧칠하기
문제: https://school.programmers.co.kr/learn/courses/30/lessons/161989
"""

def solution(n, m, section):
    ans = 1
    cur = section[0] + m - 1

    for s in section[1:]:
        if s > cur:
            cur = s + m - 1
            ans += 1

    return ans
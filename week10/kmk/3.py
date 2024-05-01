"""
기능 개발
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
"""
1. 몇일 동안 더 작업해야 하는지 갱신
2. 배포날짜 루프 돌면서 갱신
"""

def solution(p, s):
    ans = []

    for i in range(len(p)):
        m = 100 - p[i]
        p[i] = m // s[i] if m % s[i] == 0 else m // s[i] + 1

    cur, cnt = p[0], 1

    for i in range(1, len(p)):
        if cur < p[i]:
            cur = p[i]
            ans.append(cnt)
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)
    return ans
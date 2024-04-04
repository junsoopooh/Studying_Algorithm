"""
다트 게임
문제: https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""

def solution(dartResult):
    dartResult = dartResult.replace("10", "A")

    res = [10 if dartResult[0] == "A" else int(dartResult[0])]

    for s in dartResult[1:]:
        if s == "A":
            res.append(10)
        elif s.isdigit():
            res.append(int(s))
        elif s == "S":
            continue
        elif s == "D":
            res[-1] = res[-1] ** 2
        elif s == "T":
            res[-1] = res[-1] ** 3
        elif s == "*":
            res[-1] = res[-1] * 2
            if len(res) > 1:
                res[-2] = res[-2] * 2
        else:
            res[-1] = res[-1] * (-1)

    return sum(res)
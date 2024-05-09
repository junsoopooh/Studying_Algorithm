"""
괄호 변환
문제: https://school.programmers.co.kr/learn/courses/30/lessons/60058
"""

def check(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def solution(p):

    if check(p):
        return p

    def recur(p):

        if not p:
            return ""

        u, v = "", ""

        left_cnt, right_cnt = 0, 0

        for i in range(len(p)):
            if p[i] == "(":
                left_cnt += 1
            else:
                right_cnt += 1

            if left_cnt == right_cnt:
                u, v = p[:i + 1], p[i + 1:]
                break

        if check(u):
            return u + recur(v)
        else:
            s = "(" + recur(v) + ")"
            tmp_u = "".join("(" if i == ")" else ")" for i in list(u[1:len(u) - 1]))
            return s + tmp_u

    return recur(p)
"""
문자열 압축
https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""


def solution(s):
    ans = 1e9

    # 문자열 길이
    n = len(s)

    # 자를 수 있는 문자열 최대 길이는 어차피 주어진 문자열의 절반이 최대일 것.
    m = len(s) // 2

    for i in range(1, n + 1):

        res = ""

        string, number = "", 1

        flag = True

        for j in range(0, n, i):
            tmp = s[j:j + i]

            if tmp == string:
                number += 1
            else:
                if string:
                    if number != 1:
                        res += (str(number) + string)
                    else:
                        res += string
                string = tmp
                number = 1
            if len(res) > ans:
                flag = False
                break

        if flag:
            if number != 1:
                res += (str(number) + string)
            else:
                res += string

            length = len(res)

            ans = min(ans, length)

    return ans
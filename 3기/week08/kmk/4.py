"""
큰 수 만들기
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""

def solution(number, k):
    ans = []

    for n in number:
        while k and ans and ans[-1] < n:
            k -= 1
            ans.pop()
        ans.append(n)

    while k:
        k -= 1
        ans.pop()

    return "".join(ans)
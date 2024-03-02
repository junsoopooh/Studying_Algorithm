"""
점프와 순간이동
https://school.programmers.co.kr/learn/courses/30/lessons/12980
"""
def solution(n):
    ans = 0
    while n:
        if n % 2 == 0:
            n //= 2
        if n % 2 == 1:
            n -= 1
            ans += 1

    return ans
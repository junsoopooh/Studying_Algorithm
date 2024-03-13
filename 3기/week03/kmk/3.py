"""
예상 대진표
https://school.programmers.co.kr/learn/courses/30/lessons/12985
"""
def solution(n,a,b):
    # n은 페이크고 그냥 a, b 모두 짝수일때 반토막내주고 홀수일때 반토막내고 1더해주면 된다.
    answer = 0
    while a != b:
        answer += 1
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b // 2 + 1
    return answer
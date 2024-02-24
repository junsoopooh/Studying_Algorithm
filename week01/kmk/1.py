"""
정수 내림차순으로 배치하기
문제: https://school.programmers.co.kr/learn/courses/30/lessons/12933
"""
def solution(n):
    return int("".join(sorted(str(n), reverse=True)))

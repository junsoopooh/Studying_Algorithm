"""
두 정수 사이의 합
https://school.programmers.co.kr/learn/courses/30/lessons/12912
"""
def solution(a, b):
    # 그냥 루프로 푸는 것보다 훨씬 빠름
    a, b = max(a, b), min(a, b)
    return a * (a+1) // 2 - (b-1) * b // 2
"""
소수 찾기
문제: https://school.programmers.co.kr/learn/courses/30/lessons/12921
"""

def solution(n):
    prime = [1] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i + i, n + 1, i):
                prime[j] = 0

    return sum(prime[2:])
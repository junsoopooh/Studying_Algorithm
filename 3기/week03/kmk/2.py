"""
완주하지 못한 선수
https://school.programmers.co.kr/learn/courses/30/lessons/42576
"""
from collections import Counter

def solution(p, c):
    p, c = Counter(p), Counter(c)
    # value 비교해서 틀리면 걔가 범인
    for i, j in p.items():
        if c[i] != j:
            return i
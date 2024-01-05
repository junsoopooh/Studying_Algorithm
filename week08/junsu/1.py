# 문자열 내 p와 y의 개수

def solution(s):
    a = s.count('p') + s.count('P')
    b = s.count('y') + s.count('Y')
    return a == b

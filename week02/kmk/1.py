"""
하샤드 수
https://school.programmers.co.kr/learn/courses/30/lessons/12947
"""
def solution(x):
    return x % sum(int(i) for i in str(x)) == 0

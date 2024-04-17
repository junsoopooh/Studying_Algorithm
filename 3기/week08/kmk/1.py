"""
나누어 떨어지는 숫자 배열
문제 https://school.programmers.co.kr/learn/courses/30/lessons/12910
"""

def solution(arr, divisor):
    arr = sorted(i for i in arr if i % divisor == 0)
    return arr if arr else [-1]
"""
데이터 분석
문제: https://school.programmers.co.kr/learn/courses/30/lessons/250121
"""

def solution(data, ext, val_ext, sort_by):
    c = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    ext, sort_by = c[ext], c[sort_by]

    data = [i for i in data if i[ext] < val_ext]

    data.sort(key=lambda x: x[sort_by])

    return data
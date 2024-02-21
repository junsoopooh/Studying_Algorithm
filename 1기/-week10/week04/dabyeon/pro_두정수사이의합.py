a = 5
b = 3


def solution(a, b):
    ab_max = max(a, b)
    ab_min = min(a, b)

    answer = 0
    for e in range(ab_min, ab_max+1):
        answer += e

    return answer

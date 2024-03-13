def solution(a, b):
    high = max(a, b)
    low = min(a, b)
    answer = 0
    for i in range(low, high + 1):
        answer += i
    return answer

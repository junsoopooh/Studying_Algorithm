def isConsecutiveNumber(number, n):
    target = 0
    while number <= n:
        target += number
        if target == n:
            return True
        if target > n:
            return False
        number += 1
    return False


def solution(n):
    answer = 0
    for i in range(1, n):
        if isConsecutiveNumber(i, n):
            answer += 1
        else:
            pass

    return answer + 1


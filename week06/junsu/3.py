#숫자의 표현

def solution(n):
    answer = 1
    if n == 1 or n == 2:
        return answer
    tmp = 3
    while tmp <= n:
        if not n%tmp:
            answer += 1
        tmp += 2
    return answer

def solution(n):
    answer = 0
    n = list(str(n))
    print(n)
    for i in n:
        answer += int(i)
    return answer
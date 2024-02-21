def solution(x, n):
    answer = []

    if x == 0:
        a = [x] * n
        return a

    for i in range(x,x*n,x):
        answer.append(i)

    answer.append(x*n)
    return answer

print(solution(0,5))
x = 0
n = 2

def solution(x, n):
    if x == 0:
        return [0]*n

    y = x*n-1 if x < 0 else x*n+1
    answer = []
    for i in range(x, y, x):
        answer.append(i)
    return answer

print(solution(x,n))
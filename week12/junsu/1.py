# 정수 제곱근 판별
def solution(n):
    tmp = int(n**(0.5))
    if tmp**2 == n:
        answer = (tmp+1)**2
    else:
        answer = -1
    return answer

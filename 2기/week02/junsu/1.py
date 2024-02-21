# X만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    d = x
    num = x
    while len(answer) < n:
        answer.append(num)
        num += d
    return answer
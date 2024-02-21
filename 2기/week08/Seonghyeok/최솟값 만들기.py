def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    while A or B:
        answer += (A.pop() * B.pop())
    return answer
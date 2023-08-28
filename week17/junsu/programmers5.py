# 최고의 집합
def solution(n, s):
    answer = []
    tmp = s//n
    cnt = s % n
    if not tmp:
        answer = [-1]
    else:
        for i in range(n):
            answer.append(tmp)
        for i in range(1, cnt+1):
            answer[i] += 1
        answer.sort()
    return answer

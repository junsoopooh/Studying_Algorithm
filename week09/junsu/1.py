# 자릿수 더하기
def solution(n):
    answer = 0
    arr = list(str(n))
    for x in arr:
        answer += int(x)
    return answer
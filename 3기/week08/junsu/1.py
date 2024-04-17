# [나누어 떨어지는 숫자 배열](https://school.programmers.co.kr/learn/courses/30/lessons/12910)

def solution(arr, divisor):
    answer = []
    for i in arr:
        if not i%divisor:
            answer.append(i)
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]
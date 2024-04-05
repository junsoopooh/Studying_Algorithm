# [없는 숫자 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/86051)
def solution(numbers):
    answer = -1
    arr = set(numbers)
    answer = 45 - sum(arr)
    return answer

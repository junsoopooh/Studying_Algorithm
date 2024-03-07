def solution(x):
    answer = True
    arr = list(map(int, str(x)))
    tmp = sum(arr)
    if x % tmp != 0:
        answer = False
    return answer

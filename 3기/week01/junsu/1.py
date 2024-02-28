# 정수 내림차순으로 배치하기
def solution(n):
    arr = list(str(n))
    map(int, arr)
    arr.sort(reverse=True)
    map(str, arr)
    answer = "".join(arr)
    return int(answer)

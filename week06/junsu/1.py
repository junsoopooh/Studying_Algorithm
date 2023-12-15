# 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    for i in range(2,n):
        if not (n-1)%i:
            return i

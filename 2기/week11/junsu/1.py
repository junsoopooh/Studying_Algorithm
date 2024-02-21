# 자연수 뒤집어 배열로 만들기
def solution(n): 
    answer = list(str(n))
    answer.reverse()
    answer = list(map(int,answer))
    return answer

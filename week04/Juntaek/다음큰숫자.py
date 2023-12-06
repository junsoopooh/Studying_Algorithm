# def solution(n):
#     # 이진수로 변환 시 1의 갯수가 같다.
#     # 조건 1,2 만족하는 수 중 가장 작은 수.
#     answer = 0
#     return answer

def check(x):
    binary = bin(x)
    one = binary.count('1')
    return one

def solution(n):
    answer = n
    num = check(n)
    while True:
        answer += 1
        if check(answer) == num:
            return answer
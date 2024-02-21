# 다음 큰 숫자
def solution(n):
    num = str(bin(n)[2:])
    cnt = num.count('1')
    while True:
        n += 1
        tmp = str(bin(n)[2:])
        if tmp.count('1') == cnt:
            break
    answer = n
    return answer

def solution(n, a, b):
    answer = 0

    # 다음 라운드로 진출하여 새로운 번호를 부여하는 함수
    def victory(num):
        if num % 2:
            tmp = num // 2 + 1
        else:
            tmp = num // 2
        return tmp

    # 만났는지 확인하는 함수
    def check(p, q):
        if abs(p - q) == 1 and p // 2 != q // 2:
            return True
        else:
            return False

    cnt = 1
    while True:
        if check(a, b):
            return cnt
        a = victory(a)
        b = victory(b)
        cnt += 1

    return cnt

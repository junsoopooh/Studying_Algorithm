def solution(n):
    battery = 0
    while n > 0:
        if n % 2 == 0:  # 현재 위치가 짝수이면 순간이동 가능
            n //= 2
        else:  # 현재 위치가 홀수이면 한 칸 점프
            n -= 1
            battery += 1

    return battery

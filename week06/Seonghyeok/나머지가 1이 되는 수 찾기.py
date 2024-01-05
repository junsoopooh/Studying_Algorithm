def solution(n):
    x = 2
    while 1:
        if n % x == 1:
            return x
        x += 1

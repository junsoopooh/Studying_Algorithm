# [코코넛 그 두 번째 이야기](https://www.acmicpc.net/problem/6417)
import sys

def check(num: int):
    cnt = 1
    for i in range(2,num):
        tmp = num
        for _ in range(i):
            tmp -= 1
            tmp *= (i-1)
            if not tmp%i:
                tmp //= i
            else:
                break
        else:
            cnt = i
    return cnt
                

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    
    tmp = check(n)
    if tmp < 2:
        print(f"{n} coconuts, no solution")
    else:
        print(f"{n} coconuts, {tmp} people and 1 monkey")


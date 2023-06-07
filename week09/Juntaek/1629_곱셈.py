# import math
# import time
# # print(10**11%12)
# start = time.time()
# a, b, c = map(int, input().split())
# print(a**b%c)
# end = time.time()
# print(f"{end - start:.5f} sec")
# c로 나눈 나머지를 구하는 프로그램 #
import sys
input = sys.stdin.readline
a, b, c = map(int, input.split())

def multi(a, n):
    if n == 1:
        return a%c
    else:
        tmp = multi(a, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c
print(multi(a, b))

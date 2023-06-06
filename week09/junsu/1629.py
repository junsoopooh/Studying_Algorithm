import sys

a, b, c = map(int, sys.stdin.readline().split())


def divide(x,y):
    if y == 1:
        return x
    else:

        if y % 2 == 0:
            (((divide(x,y//2))% c) * (divide(x,y//2)% c)) % c
        else:
            ((divide(x,y//2)%c)* (divide(x,y//2)%c)*x) % c


num = divide(a,b)
print(num)

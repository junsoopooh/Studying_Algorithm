import sys

x,y = map(int,sys.stdin.readline().split())

def ans(n):
    if n%7 == 0:
        print('MON')
    elif n%7 == 1:
        print('TUE')
    elif n%7 == 2:
        print('WED')
    elif n%7 == 3:
        print('THU')
    elif n%7 == 4:
        print('FRI')
    elif n%7 == 5:
        print('SAT')
    elif n%7 == 6:
        print('SUN')

def calculate(x,y):
    if x <= 2:
        day = y-1 + 31*(x-1)
        ans(day)
    elif 2<x<=7:
        day = 31 + 28 + y-1 + 31*((x-2)//2) + 30*((x-3)//2)
        ans(day)
    else:
        day = 31 + 28 + 31 + 30 + 31 + 30 + 31+ y-1 + 31*((x-7)//2) + 30*((x-8)//2)
        ans(day)

calculate(x,y)



import sys
y, m, d = map(int, sys.stdin.readline().split())
d_y, d_m, d_d = map(int, sys.stdin.readline().split())

def cal_year(a, b):
    x = b - a
    cnt_y_1 = x // 4
    cnt_y_2 = x // 100
    cnt_y_3 = x // 400
    cnt_y = cnt_y_1 - cnt_y_2 + cnt_y_3
    return 365*x + cnt_y

def month(x):
    if x == 2:
        return 28
    elif x % 2:
        return 31
    elif x == 8:
        return 31
    elif not x % 2:
        return 30

def cal_month(a, b):
    cnt = 0
    if a > b:
        while a != b:
            a -= 1
            cnt -= month(a)
    else:
        while a != b:
            a += 1
            cnt += month(a)
    return cnt

def cal_day(a, b):
    return b-a

if d_y-y >= 1001:
    print('gg')
elif d_y-y == 1000:
    if d_m > m:
        print('gg')
    elif d_m == m:
        if d_d >= d:
            print('gg')
else:
    ans = 1
    ans += cal_year(y, d_y) + cal_month(m, d_m) + cal_day(d, d_d)
    print('D-'+str(ans))
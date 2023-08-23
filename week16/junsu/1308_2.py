import sys
start_year, start_month, start_day = map(int, sys.stdin.readline().split())
end_year, end_month, end_day = map(int, sys.stdin.readline().split())

def check_year(x):
    if x%4:
        return False
    else:
        if x%100:
            return True
        else:
            if x%400:
                return False
            else:
                return True

def calculate(a,b,c):
    tmp = 0
    for i in range(1,a):
        if check_year(i):
            tmp += 366
        else:
            tmp += 365

    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,b):
        tmp += month[i]
        if i == 2 and check_year(a) == True:
            tmp += 1    

    tmp += (c-1)
    return tmp

def answer(a,b,c,d,e,f):
    ans = calculate(d,e,f) - calculate(a,b,c)
    print(f"D-{ans}")
    return

if end_year-start_year > 1000:
    print("gg")
elif end_year-start_year == 1000:
    if end_month>start_month:
        print("gg")
    elif end_month==start_month:
        if end_day >= start_day:
            print("gg")
        else:
            answer(start_year,start_month,start_day,end_year,end_month,end_day)
    else:
        answer(start_year,start_month,start_day,end_year,end_month,end_day)
else:
    answer(start_year,start_month,start_day,end_year,end_month,end_day)
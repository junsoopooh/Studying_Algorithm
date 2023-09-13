import sys

while True:
    try:
        one, num = map(int, input().split('/'))
        cnt = 0
        a = num*2+1
        while a > num:
            if not (num*a) % (a-num):
                cnt += 1
            a -= 1
        print(cnt)
    except:
        break

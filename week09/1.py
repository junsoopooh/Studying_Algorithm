# 정제헌을 팔자!

# 실패 코드
import sys
while True:
    try:
        tmp = sys.stdin.readline()
        arr = set()
        n = int(tmp[2:])
        if n == 1:
            print(1)
            continue
        i = n
        while True:
            i += 1
            a = (n*i)//(i-n)
            b = (n*i) % (i-n)
            print(a, b)
            if a == n:
                print(a, b, n)
                break
            if not b:
                p = [i, a]
                p.sort()
                arr.add(p)

        print(len(arr), arr)
    except:
        break

# 정답 코드
# pypy3로 제출할 것

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

import sys
while True:
    try:
        o, n = map(int, sys.stdin.readline().split('/'))
        cnt = 0

        if n > 2:
            x = 2
            y = (n**2)/(x-n)+n
            while y > 0 and x < n:
                if not (n**2) % (x-n):
                    cnt += 1
                x += 1

        x = n+1
        y = (n**2)/(x-n)+n
        while (n**2)/(x-n) > 1:
            if not (n**2) % (x-n):
                cnt += 1
            x += 1
        print(cnt)
    except:
        break

import sys

c = int(sys.stdin.readline())
for _ in range(c):
    result = list(map(int,sys.stdin.readline().split()))
    num = result[0]
    total = sum(result[1:])
    avg = total // num
    cnt = 0
    for i in range(1,len(result)):
        if result[i] > avg:
            cnt += 1
    ans = cnt/num*100
    print("{:.3f}".format(ans),end='%\n')
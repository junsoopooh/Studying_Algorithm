import sys

n,k = map(int,sys.stdin.readline().split())
num = int(sys.stdin.readline())
num = list(str(num))

tmp = num[0]
arr = []
cnt = 0
while k > 0:
    tmp = num[cnt]
    flag = False
    for i in range(1+cnt,k+cnt+1):
        if tmp < num[i]:
            tmp = num[i]
            cnt = i
            flag = True
    if flag:
        arr.append(tmp)
        k -= cnt
    else:
        cnt += 1
    if k == 0:
        break
print(*arr, sep='')
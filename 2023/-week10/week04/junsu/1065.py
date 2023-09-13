import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1,int(n)+1):
    if i < 100:
        cnt += 1
        continue
    else:
        if i//100-(i%100)//10 == (i%100)//10-(i%100)%10:
            cnt += 1
print(cnt)

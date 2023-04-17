import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in nums:
    if i == 1:
        continue
    elif i == 2:
        cnt += 1
        continue
    elif i == 3:
        cnt += 1
        continue
    else:
        if i%2 != 0:
            for j in range(3,i//2):
                if i%j == 0:
                    cnt -= 1
                    break
            cnt += 1
print(cnt)
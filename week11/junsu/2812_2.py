import sys

n, k = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline().rstrip())
stk = [num[0]]
tmp = 0
cnt = 0
for i in range(1, n):
    if cnt == k or n-i:
        stk.append(num[i])
        continue
    if stk[-1] < num[i]:
        stk.pop()
        stk.append(num[i])
        cnt += 1
    elif stk[-1] == num[i]:
        stk.append(num[i])
    else:
        cnt += 1

print(*stk, sep='')

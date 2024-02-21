import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

arr = deque()
ans = []
ans.append('<')

for i in range(1,n+1):
    arr.append(i)

cnt = 1
while arr:
    if cnt == k:
        tmp = arr.popleft()
        tmp = str(tmp)+','+' '
        ans.append(tmp)
        cnt = 1
    else:
        tmp = arr.popleft()
        arr.append(tmp)
        cnt += 1
q = ans.pop()
ans.append(q[0])
ans.append('>')
print(*ans,sep='')

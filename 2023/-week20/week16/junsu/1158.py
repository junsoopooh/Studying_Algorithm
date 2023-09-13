import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())

arr = deque()
for i in range(1,n+1):
    arr.append(str(i))

ans = []
cnt = 0
while arr:
    tmp = arr.popleft()
    cnt += 1
    if cnt%k:
        arr.append(tmp)
    else:
        ans.append(tmp)
ans = ', '.join(ans)
print('<',ans,'>',sep='')
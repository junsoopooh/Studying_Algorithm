import sys
from collections import deque

s = list(sys.stdin.readline().rstrip())
arr = deque(s)
n = len(s)
lst = []
lst.append(arr.popleft())
cnt = 0
while arr:
    tmp = arr[0]
    if not lst or tmp == '(':
        tmp = arr.popleft()
        lst.append(tmp)
    elif tmp == ')':
        if lst[-1] == '(':
            lst.pop()
            arr.popleft()
            cnt += 1
        else:
            arr.popleft()
answer = 2**cnt
answer %= 1000000007
print(answer)
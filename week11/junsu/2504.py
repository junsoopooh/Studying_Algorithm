import sys

str = sys.stdin.readline().rstrip()
arr = []
ans = 0
tmp = 1
for i in range(len(str)):
    if i and len(arr) == 0:
        ans += tmp
        tmp = 1
    k = str[i]
    if k == '(':
        arr.append(k)
    elif k == '[':
        arr.append(k)
    elif k == ')':
        if arr[-1] == '[':
            ans = 0
            break
        else:
            arr.pop()
            tmp *= 2
    else:
        if arr[-1] == '(':
            ans = 0
            break
        else:
            arr.pop()
            tmp *= 3
if not arr:
    print(ans)
else:
    print(0)
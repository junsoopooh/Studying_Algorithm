import sys

s = sys.stdin.readline().rstrip()
n = len(s)
stk = []
arr = []
cnt = 0
for i in range(n):
    if s[i] == '(':
        stk.append('(')
    else:
        if stk:
            stk.pop()
            cnt += 1
            
    if i and not stk:
        arr.append(cnt)
        cnt = 0
print(arr)
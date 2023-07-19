import sys

a = sys.stdin.readline().rstrip()
stk = []
cnt = 0
for i in range(len(a)):
    if i and not stk and cnt != 1:
        0
    val = a[i]
    if val == '(':
        cnt += 2
        stk.append(val)
    elif val == '[':
        cnt += 3
        stk.append(val)
    elif val == ')':
        tmp = stk.pop()
        if tmp == '(':
            if not cnt:
                cnt += 2
            else:
                cnt *= 2
        else:
            cnt = 0
            break
    elif val == ']':
        tmp = stk.pop()
        if tmp == '[':
            if not cnt:
                cnt += 3
            else:
                cnt *= 3
        else:
            cnt = 0
            break
print(cnt)
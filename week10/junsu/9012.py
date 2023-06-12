import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ps = list(sys.stdin.readline().rstrip())
    stk = []
    ans = 'YES'
    for i in ps: 
        if i == '(':
            stk.append(i)
        else:
            if not stk:
                ans = 'NO'
                break
            else:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    ans = 'NO'
                    stk.clear()
                    break
    if stk :
        print('NO')
    else:
        print(ans)

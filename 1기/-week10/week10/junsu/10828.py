import sys

n = int(sys.stdin.readline())
stk = []
k = []
for _ in range(n):
    k = list(sys.stdin.readline().split())
    order = k[0]
    if order == 'push':
        stk.append(k[1])
    elif order == 'pop':
        if stk :
            tmp = stk.pop()
            print(tmp)
        else:
            print(-1)
    elif order == 'size':
        print(len(stk))
    elif order == 'empty':
        if not stk:
            print(1)
        else:
            print(0)
    else:
        if stk:
            print(stk[-1])
        else:
            print(-1)
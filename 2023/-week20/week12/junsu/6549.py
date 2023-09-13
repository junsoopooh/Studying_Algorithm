import sys
while True:
    case = list(map(int,sys.stdin.readline().split()))
    n = case[0]
    if n == 0:
        break
    squares = case[1:]
    stk = []
    max_val = 0
    for i in range(n):
        h = squares[i]
        stk.append([h,1])
        if not stk:
            continue
        for j in stk:
            if j[0] == 0:
                continue
            if h >= j[0]:
                j[1] += 1
            else:
                val = j[0]*j[1]
                max_val = max(max_val,val)
                j[0] = 0
    for k in stk:
        tmp = k[0]*k[1]
        max_val = max(max_val,tmp)
    print(max_val)
import sys

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    n = arr[0]
    if n == 0:
        break
    stk = []
    ans = 0
    for i in range(n+1):
        if i == 0:
            continue
        h = arr[i]
        if stk and stk[-1][0] > h:
            while stk:
                tmp = stk.pop()
                if stk:
                    dif = stk[-1][1]+1
                else:
                    dif = 1
                cnt = tmp[0]*(i-dif)
                ans = max(ans,cnt)
                if not stk or stk[-1][0] <= h:
                    break
        if not stk or stk[-1][0] <= h:
            stk.append([h,i])
    while stk:
        tmp = stk.pop()
        if stk:
            dif = stk[-1][1]+1
        else:
            dif = 1
        cnt = tmp[0]*(n+1-dif)
        ans = max(ans,cnt)
    print(ans)

# 14번 ,25번 조건을 위아래 바꾸니 정답이 되었다. 왜그럴까
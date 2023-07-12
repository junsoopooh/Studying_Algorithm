import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
stk = []
ans = [0 for _ in range(n)]
for i in range(n):
    while stk:
        if stk[-1][1] > towers[i]: # 0번째 : index , 1번째 : 높이
            ans[i] = stk[-1][0] + 1 # 몇번쨰 타워인지와 index는 1차이나니까
            break
        else:
            stk.pop()
    stk.append([i, towers[i]])

print(*ans)
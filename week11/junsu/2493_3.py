import sys

n = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
ans = [0 for _ in range(n)]
stk = []
stk.append(n-1)
for i in range(n-2,-1,-1):
    j = len(stk)-1
    while j >= 0:
        tmp = stk[j]
        if towers[i] >= towers[tmp]:
            tgt = stk.pop(j)
            ans[tgt] = i+1
        j -= 1
    stk.append(i)
print(ans)
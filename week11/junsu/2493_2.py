import sys 

n = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
stk = [n-1]
ans = [0 for _ in range(n)]

for i in range(n-2,-1,-1):
    for j in stk[-1::-1]:
        if towers[j] <= towers[i]:
            ans[j] = i+1
            stk.pop()
        stk.append(i)
print(*ans)
import sys
sys.setrecursionlimit(10**6)

n,m = map(int,sys.stdin.readline().split())
arr_h = [[] for _ in range(n+1)]
arr_l = [[] for _ in range(n+1)]
for _ in range(m):
    heavy,light = map(int,sys.stdin.readline().split())
    arr_h[heavy].append(light)
    arr_l[light].append(heavy)

def dfs(i):
    global cnt
    check = [0 for _ in range(n+1)]
    for x in arr_h[i]:
        check[x] = 1
        for j in arr_h[x]:
            if not check[j]:
                check[j] = 1
    if num <= sum(check):
        cnt += 1
        return

    check = [0 for _ in range(n+1)]
    for x in arr_l[i]:
        check[x] = 1
        for j in arr_l[x]:
            if not check[j]:
                check[j] = 1
    if num <= sum(check):
        cnt += 1
cnt = 0
num = n//2 + 1
for i in range(1,n+1):
    dfs(i)
print(cnt)
import sys
sys.setrecursionlimit(10**6)

n,m =map(int,sys.stdin.readline().split())
arr_h=[[] for _ in range(n+1)]
arr_l=[[] for _ in range(n+1)]

for i in range(m):
    heavy,light=map(int,input().split())
    arr_h[heavy].append(light)
    arr_l[light].append(heavy)

def dfs(arr, n):
    global cnt
    for i in arr[n]:
        if not visited[i]:
            visited[i]=True
            cnt += 1
            dfs(arr,i)

num= n//2 + 1
ans=0

for i in range(1,n+1):
    visited = [False for _ in range(n+1)]

    cnt = 0
    dfs(arr_h,i)

    if cnt >= num:
        ans += 1
        
    cnt = 0
    dfs(arr_l,i)
    if cnt >= num:
        ans += 1

print(ans)
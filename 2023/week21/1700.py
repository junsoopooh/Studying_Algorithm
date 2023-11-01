import sys

n, k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

tmp = []
cnt = 0
for i in range(k):
    if arr[i] in tmp:
        continue
    
    if len(tmp) < n:
        tmp.append(arr[i])
        continue
    
    idx = []
    
    for j in tmp:
        if j in arr[i:]:
            idx.append(arr[i:].index(j))
        else:
            idx.append(101)
    val = idx.index(max(idx))
    tmp.remove(tmp[val])
    tmp.append(arr[i])
    cnt += 1

print(cnt)
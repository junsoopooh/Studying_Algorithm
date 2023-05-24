import sys

n, m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

left = 0
right = 10**6
max_val = 0
while left <= right:
    total = 0
    mid = (left + right) //2
    for x in trees:
        if x > mid:
            tmp = x-mid
            total += tmp
    if total > m:
        max_val = max(mid,max_val)
        left = mid+1
    elif total < m:
        right = mid-1
    else:
        max_val = mid
print(max_val)
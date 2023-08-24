import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for target in range(1, n):
        for i in range(target-1, n):
            if arr[i] == target:
                idx = i
                break
        while idx != target-1:
            cnt += 1
            if idx > target-1:
                tmp = arr[idx-1]
                arr[idx-1] = target
                arr[idx] = tmp
                idx -= 1
            else:
                tmp = arr[idx+1]
                arr[idx+1] = target
                arr[idx] = tmp
                idx += 1
    print(cnt)

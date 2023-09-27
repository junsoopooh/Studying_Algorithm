import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [0 for _ in range(n+1)]
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        arr[a] = b
    cnt = 0
    for i in range(1, n+1):
        if i == 1:
            cnt += 1
            limit = arr[i]
        else:
            if arr[i] < limit:
                cnt += 1
                limit = arr[i]
            else:
                continue

    print(cnt)

import sys
sys.setrecursionlimit(10**9)
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [[0, 0] for _ in range(n+1)]
    arr[0][0] = 1
    for i in range(1, n+1):
        arr[i][0] = arr[i-1][1]
        arr[i][1] = arr[i-1][0] + arr[i-1][1]
    print(arr[n][0], arr[n][1], sep=' ')

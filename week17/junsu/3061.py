import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    ans = [0 for _ in range(n)]
    while 0 in ans:
        for i in range(n):
            if arr[i] == i+1:
                ans[i] = i+1
            else:
                tmp = arr[i]
                while True:
                    if tmp == arr[i+1]:
                        break
                    if tmp > arr[i+1]:
                        arr[i] = arr[i+1]
                        arr[i+1] = tmp
                        i += 1
                        cnt += 1
                    elif tmp < arr[i+1]:
                        arr[i] = arr[i-1]
                        arr[i-1] = tmp
                        i -= 1
                        cnt += 1
            
    print(cnt)
        
            
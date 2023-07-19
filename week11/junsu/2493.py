import sys

n = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
arr = []
result = [0] * n
for i in range(n-1,-1,-1):
    if i == n-1:
        tmp = towers[i]
        arr.append(i)
        continue
    else:
        arr.append(i)
        if towers[i] >= tmp:
            tmp = towers[i]
            for j in arr:
                if towers[j] <= tmp:
                    arr.remove(j)
                    result[j] = i+1
 
print(*result, sep=' ')
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n): 
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort()
arr.sort(key = lambda  x : x[1])
cnt = 1
t = arr[0][1]

for i in range(1,n):
    if arr[i][0] >= t:
        t = arr[i][1]
        cnt += 1
print(cnt)
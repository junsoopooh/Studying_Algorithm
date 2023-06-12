import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
cnt = 1
tmp = arr[-1]
for i in range(n-1,-1,-1):
    if arr[i] > tmp:
        cnt += 1
        tmp = arr[i]
print(cnt)
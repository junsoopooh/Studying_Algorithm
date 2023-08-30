import sys

word = list(sys.stdin.readline().rstrip())
bomb = sys.stdin.readline().rstrip()
n = len(bomb)
arr = []
ans = ''.join(word[:3])


for i in range(len(word)):
    arr.append(word[i])
    if len(arr) < n:
        continue
    k = len(arr)
    tmp = ''.join(arr[k-n:])
    if tmp == bomb:
        for _ in range(n):
            arr.pop()

if arr:
    print(*arr,sep='')
else:
    print('FRULA')

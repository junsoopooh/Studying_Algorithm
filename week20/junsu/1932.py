import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    if i == 0:
        arr.append([int(sys.stdin.readline())])
        continue
    tmp = sys.stdin.readline().rstrip()
    arr.append(list(tmp.split(' ')))
    for x in range(len(arr[-1])):
        arr[-1][x] = int(arr[-1][x])

for i in range(n):
    if not i:
        continue
    j = 0
    while j < len(arr[i]):
        tmp = []
        if j-1 >= 0:
            tmp.append(arr[i-1][j-1])
        if j < len(arr[i-1]):
            tmp.append(arr[i-1][j])
        if tmp:
            arr[i][j] += max(tmp)
        j += 1

print(max(arr[-1]))

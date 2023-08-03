import sys

arr = []
while True:
    num = sys.stdin.readline().rstrip()
    if not num:
        break
    arr.append(int(num))

n = len(arr)
tree = [[arr[0],0,0]]
tree = [[0, 0, 0] for _ in range(n-1)]
for i in range(1,n):
    tree[i][0] = arr[i]
    if arr[i-1] > arr[i]:
        tree[i-1][1] = arr[i]
    else:
        tmp = arr[i+1]
        for j in range(n-1):
            if arr[j] < tmp:
                tree[j][2] = tmp
                break
print(tree)

import sys

arr = []
n = int(sys.stdin.readline())
for _ in range(n):
    p, l, r = sys.stdin.readline().rstrip().split()
    arr.append([p, l, r])

front = []
mid = []
back = []

def search_front(node, arr, ans):
    ans.append(node[0])
    if node[1] != '.':
        for x in arr:
            if x[0] == node[1]:
                search_front(x, arr, ans)
                break
    if node[2] != '.':
        for x in arr:
            if x[0] == node[2]:
                search_front(x, arr, ans)
                break

def search_mid(node, arr, ans):
    if node[1] != '.':
        for x in arr:
            if x[0] == node[1]:
                search_mid(x, arr, ans)
                break
    ans.append(node[0])
    if node[2] != '.':
        for x in arr:
            if x[0] == node[2]:
                search_mid(x, arr, ans)
                break

def search_back(node, arr, ans):
    if node[1] != '.':
        for x in arr:
            if x[0] == node[1]:
                search_back(x, arr, ans)
                break
    if node[2] != '.':
        for x in arr:
            if x[0] == node[2]:
                search_back(x, arr, ans)
                break
    ans.append(node[0])

search_front(arr[0], arr, front)
search_mid(arr[0], arr, mid)
search_back(arr[0], arr, back)
print(*front, sep='')
print(*mid, sep='')
print(*back, sep='')

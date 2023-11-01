import sys

arr = []
n = int(sys.stdin.readline())
for _ in range(n):
    p, l, r = sys.stdin.readline().rstrip().split()
    arr.append([p, l, r])

front = ['A']
mid = []
back = []


def search_front(node, arr, ans):
    for x in arr:
        if x[0] == node[0]:
            if x[1] != '.':
                ans.append(x[1])
                search_front(x, arr, ans)
            if x[2] != '.':
                ans.append(x[2])
                search_front(x, arr, ans)


def search_mid(node, arr, ans):
    for x in arr:
        if x[0] == node[0]:
            if x[1] != '.':
                search_mid(x, arr, ans)
            else:
                ans.append(x[0])
                if x[2] != '.':
                    search_mid(x, arr, ans)
            break


def search_back(node, arr, ans):
    for x in arr:
        if x[0] == node[0]:
            if x[1] != '.':
                search_back(x, arr, ans)
            else:
                ans.append(node)

            if x[2] != '.':
                search_back(x, arr, ans)
                ans.append(x)
            ans.append(node[0])


search_front(arr[0], arr, front)
search_mid(arr[0], arr, mid)
search_back(arr[0], arr, back)
print(front)
print(mid)
print(back)

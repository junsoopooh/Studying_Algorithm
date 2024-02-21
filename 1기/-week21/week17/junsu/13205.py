import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k, n, l_1, l_2 = map(int, sys.stdin.readline().split())
    ranks = list(map(int, sys.stdin.readline().split()))

    for i in range(n, -1, -1):
        if i in ranks:
            start = i
            break
    mid = k//2 + 1

    def make_password(x):
        tmp_arr = []
        while len(tmp_arr) < l_2 and x <= n-1:
            if ranks[x] >= mid:
                tmp_arr.append(ranks[x])
            else:
                break
            x += 1
        if len(tmp_arr) >= l_1:
            return tmp_arr
        else:
            return

    def change(a, b):
        d = len(a)
        for i in range(d):
            if a[i] > b[i]:
                return a
            elif a[i] < b[i]:
                return b
        return False

    arr = []
    cnt = 1
    for i in range(n):
        if ranks[i] != start:
            continue
        if make_password(i):
            if not arr:
                arr.append(make_password(i))
            else:
                if len(make_password(i)) > len(arr[0]):
                    arr.pop()
                    arr.append(make_password(i))
                    cnt = 1
                elif len(make_password(i)) == len(arr[0]):
                    if change(make_password(i), arr[0]) == arr[0] or not change(make_password(i), arr[0]):
                        cnt += 1
                    else:
                        cnt = 1
                        arr.pop()
                        arr.append(make_password(i))
    print(cnt)

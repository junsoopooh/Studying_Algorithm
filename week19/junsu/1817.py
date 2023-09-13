import sys

n, m = map(int, sys.stdin.readline().split())
if n == 0:
    print(0)
else:
    books = list(map(int, sys.stdin.readline().split()))

    stk = []
    cnt = 0
    for i in range(len(books)):
        if not stk:
            stk.append(books[i])
            cnt += 1
            continue
        if sum(stk) + books[i] > m:
            stk.clear()
            cnt += 1
            stk.append(books[i])
        elif sum(stk) + books[i] == m:
            stk.clear()
        else:
            stk.append(books[i])
    print(cnt)

n, x = map(int, input().split())
a = list(map(int, input().split()))
# print(a)
for i in a:
    if i < x:
        print(i, end=' ')
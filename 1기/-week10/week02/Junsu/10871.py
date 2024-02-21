import sys

n,x = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
ans = []
for i in a:
    if i < x:
        ans.append(i)
print(*ans, sep=' ')
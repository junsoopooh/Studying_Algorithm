import sys

a, b = map(str, sys.stdin.readline().rstrip().split())
for i in range(1, 4):
    if int(a[-i]) > int(b[-i]):
        ans = a
        break
    elif int(a[-i]) < int(b[-i]):
        ans = b
        break
print(ans[::-1])

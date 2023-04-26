import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
num = a*b*c
s_num = str(num)
arr = list(s_num)
for i in range(10):
    s_i = str(i)
    ans = arr.count(s_i)
    print(ans)
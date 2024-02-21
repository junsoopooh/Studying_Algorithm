import sys

a,b,v = map(int,sys.stdin.readline().split())
if (v-a)%(a-b) != 0:
    ans = (v-a)//(a-b) + 2
else:
    ans = (v-a)//(a-b) + 1
print(ans)